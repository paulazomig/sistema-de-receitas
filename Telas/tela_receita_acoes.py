from Telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaReceitaAcoes(AbstractTela):

    def __init__(self):
        self.__window = None
        self.__window_ingrediente = None
        self.init_components(None, None)
        self.ingredientes_tela = ''

    def init_components(self, lista_ingredientes, infos_tela):
        if not infos_tela:
            layout = [[sg.Text('Nova Receita')],
                      [sg.Text('Título:'), sg.InputText(key='titulo')],
                      [sg.Text('Ingredientes:')],
                      [sg.Text('Modo de Preparo:')],
                      [sg.Multiline(size=(70,7), key='preparo')],
                      [sg.Button('Adicionar Ingredientes'), sg.Button('Cancelar',key='cancel')]]
        else:
            layout = [[sg.Text('Nova Receita')],
                      [sg.Text('Título:'), sg.InputText(infos_tela['titulo'], key='titulo')],
                      [sg.Text('Ingredientes:')],
                      [sg.Text('Modo de Preparo:')],
                      [sg.Multiline(infos_tela['preparo'], size=(70,7), key='preparo')],
                      [sg.Button('Adicionar Ingredientes'), sg.Button('Cancelar',key='cancel')]]

        layout_ingredientes = [[sg.Text('Cadastro de Ingrediente da Receita')],
                               [sg.Text('Ingrediente:'), sg.InputCombo(lista_ingredientes, size=(50, 1), key='cb_opcao')],
                               [sg.Text('Quantidade'), sg.InputText(key='quantidade', size=(25,1))],
                               [sg.Text('\nCaso o ingrediente que deseja não seja encontrado na lista é preciso '
                                        '\ncastrá-lo antes de seguir com o cadastro da receita.')],
                               [sg.Button('Adicionar Mais Ingredientes', key='adicionar'),
                                sg.Button('Finalizar Cadastro da Receita', key='finalizar'),
                                sg.Button('Cancelar', key='cancel')]]

        self.__window = sg.Window('Cadastro de Receita',
                                  location=(450, 300),
                                  default_element_size=(60, 1)).Layout(layout)

        self.__window_ingrediente = sg.Window('Cadastro de Ingredientes da Receita',
                                              location=(450, 300),
                                              default_element_size=(60, 1)).Layout(layout_ingredientes)

    def abre_tela(self, lista_ingredientes, infos_tela):
        self.init_components(lista_ingredientes, infos_tela)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'cancel':
            return button, None
        elif not button:
            exit(0)
        else:
            if values['titulo'] == '':
                self.erro_cadastro()
                return button, None
            else:
                ingredientes_receita = {}
                loop = True
                while loop:
                    button_tela_ing, values_tela_ing = self.__window_ingrediente.Read()
                    if button_tela_ing == 'cancel':
                        self.__window_ingrediente.Close()
                        return button_tela_ing, None
                    elif not button_tela_ing:
                        exit(0)

                    else:
                        try:
                            qtd = int(values_tela_ing['quantidade'])
                        except Exception:
                            self.erro_valor()
                            continue

                        if values_tela_ing['cb_opcao'] != '':
                            nome = values_tela_ing['cb_opcao'].split(',')
                            ingredientes_receita[nome[0]] = qtd

                            if button_tela_ing == 'finalizar':
                                loop = False
                                self.__window_ingrediente.Close()
                                self.feedback_sucesso()
                            else:
                                self.__window_ingrediente.FindElement('cb_opcao').Update('')
                                self.__window_ingrediente.FindElement('quantidade').Update('')

                                self.feedback_sucesso()
                        else:
                            self.erro_cadastro()
                            return button_tela_ing, None
                infos_receita = {'titulo': values['titulo'], 'ingredientes_receita': ingredientes_receita,
                                 'preparo': values['preparo']}
                return button, infos_receita

    # ------ MÉTODOS TRATAMENTO EXCEÇÕES ------

    def erro_ja_cadastrado(self, nome):
        sg.Popup("Item Já Cadastrado",
                 "Não é possível completar a operação -  a receita {} já foi cadastrada.\n".format(nome), location=(500,300))

    def erro_cadastro(self):
        sg.Popup("Erro de Cadastro", "Atenção! O valor de título da receita não deve ser vazio. "
                                     "O valor de quantidade de ingrediente deve ser um "
                                     "número inteiro >= 0. Tente novamente.", location=(500,300))