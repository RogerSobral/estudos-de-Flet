from ...views.login import Login
from ...controllers.loginController import LoginController
from src.models.DAO.users import UserModal
from src.models.DAO.conn import ConnectionClass
def loginConstructo()-> Login:

    telaLogin:Login = Login()
    modalUsuario=UserModal()
    conn = ConnectionClass(r"sqlite:///src/models/entity/financas.db")
    controllerLogin=LoginController(telaLogin,modalUsuario,conn)


    return telaLogin