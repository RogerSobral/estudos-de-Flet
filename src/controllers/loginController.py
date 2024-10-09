from src.views.login import Login

from src.models.entity.user import User
class LoginController:

    def __init__(self,infoTelaLogin:Login)->None:
        super().__init__()

        self.infoView=infoTelaLogin
        self.infoView.btn_enter.on_click=self.intoSystem

    def intoSystem(self, e)->None:

        self.infoView.page.go("/menu")



