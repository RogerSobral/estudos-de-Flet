from ...views.login import Login
from ...controllers.loginController import LoginController

def loginConstructo()-> Login:

    telaLogin:Login = Login()
    controllerLogin=LoginController(telaLogin)


    return telaLogin