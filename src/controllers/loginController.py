from src.views.login import Login
from src.models.userModel import UserModel
from src.models.entity.user import User
class LoginController:

    def __init__(self,infoTelaLogin:Login, userModel:UserModel)->None:
        super().__init__()
        self.userModel=userModel
        self.infoView=infoTelaLogin
        self.infoView.btn_enter.on_click=self.entrarSistema

    def entrarSistema(self,e):

        for user in self.userModel.get_all_users():
            singleUser=User(login=user[1],password=user[2])

            if self.infoView.name.value==singleUser.login and self.infoView.password.value==singleUser.password:
                self.infoView.page.go("/menu")

