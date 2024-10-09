from ...views.login import Login
from ...controllers.loginController import LoginController
from src.models.entity.users import UserModal
def loginConstructo()-> Login:

    telaLogin:Login = Login()
    modalUsuario=UserModal()
    controllerLogin=LoginController(telaLogin,modalUsuario)


    return telaLogin