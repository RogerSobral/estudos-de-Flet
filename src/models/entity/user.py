class User:
    def __init__(self, login:str, password:str)->None:
        self.__login=login
        self.__password=password


    @property
    def login(self)->str:
        return self.__login

    @login.setter
    def login(self,login) ->None:
        self.__login=login

    @property
    def password(self)->str:
        return self.__password

    @password.setter
    def password(self,password):
        self.__password=password