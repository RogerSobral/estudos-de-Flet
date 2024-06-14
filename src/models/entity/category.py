
class Category:

    def __init__(self,id:int, name:str )-> None:
        self.__id=id
        self.__name=name


    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name=name