from src.views.login import Login

class LoginController:

    def __init__(self,infoTelaLogin:Login):
        super().__init__()
        # self.model=model
        self.infoView=infoTelaLogin
        self.infoView.btn_enter.on_click=self.entrarSistema

    def entrarSistema(self,e):
        self.infoView.page.go("/menu")

