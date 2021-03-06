from abc import ABC, abstractmethod
import pickle
from Excecoes.no_key_exception import NoKeyException


class AbstractDAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            raise NoKeyException()

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            raise NoKeyException()

    def get_all(self):
        return self.__cache.values()

    def get_all_names(self):
        list = []
        for i in self.__cache:
            list.append(i)
        return list
