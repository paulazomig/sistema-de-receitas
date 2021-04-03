class TelaReceita:
    def tela_opcoes(self):
        print("Escolha Opção:\n1. Cadastrar Receitas\n2. Alterar Cadastro de Receita\n3. Listar "
              "Receitas\n4. Excluir Receita\n0. Retornar ao Menu Principal")
        opcao = int(input())#tratar exceções
        return opcao

    def obter_dados_receita(self):
        print("CADASTRO DE RECEITA:")
        titulo = input("Título da receita: ")

        print("Ingredientes:")
        continua = True
        ingredientes_e_quantidades = {}
        while continua:
            nome_ingrediente = input("Nome do ingrediente: ")
            quantidade_ingrediente = int(input("Quantidade do ingrediente: "))

            ingredientes_e_quantidades[nome_ingrediente] = quantidade_ingrediente

            mais_ingredientes = input("Deseja adicionar mais um ingrediente? ")
            if mais_ingredientes == "Não":
                continua = False
        print(ingredientes_e_quantidades)
        preparo = input("Modo de preparo: ")

        return {"titulo": titulo, "ingredientes_e_quantidades": ingredientes_e_quantidades, "preparo": preparo}

    def alterar_receita(self):
        print("Qual receita deseja alterar?")
        titulo = input("Titulo: ")
        return titulo

    def listar_receitas(self):
        pass

    def excluir_receita(self):
        print("EXCLUIR RECEITA:")
        titulo_excluido = input("Nome da receita a ser excluída: ")
        return titulo_excluido
