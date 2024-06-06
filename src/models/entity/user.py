class User:
    def __init__(self, login:str, password:str)->None:
        self.__login=login
        self.__password=password


    @property
    def login(self)->str:
        return self.__login

