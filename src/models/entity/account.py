
class Account:

    def __init__(self, id: int, name: str) -> None:
        self.__id:int = id
        self.__name:str = name
        self.__value:float=0

    @property
    def id(self)->int:
        return self.__id

    @property
    def name(self)->str:
        return self.__name

    @name.setter
    def name(self, name:str)-> None:
        self.__name = name

    @property
    def value(self)-> float:
        return self.__value