from ...views.login import Login
from ...controllers.loginController import LoginController
from src.models.userModel import UserModel
def loginConstructo()-> Login:

    telaLogin:Login = Login()
    userModel=UserModel()
    loginController=LoginController(telaLogin,userModel)


    return telaLogin