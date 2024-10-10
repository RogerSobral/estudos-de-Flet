from src.views.login import Login

from src.models.DAO.conn import ConnectionClass
from src.models.DAO.users import UserModal

class LoginController:

    def __init__(self,infoTelaLogin:Login,modalUsuario:UserModal,conn:ConnectionClass)->None:
        super().__init__()
        self.conn=conn
        self.modalUsuario=modalUsuario
        self.infoView=infoTelaLogin
        self.infoView.btn_enter.on_click=self.intoSystem

    def intoSystem(self, e)->None:
        self.conn.connect()
        session = self.conn.get_session()
        usuarios = session.query(UserModal).all()
        for usuario in usuarios:
            if (usuario.nome == self.infoView.name.value) and (usuario.senha==self.infoView.password.value):
                print(f'ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.senha}')
                self.infoView.page.go("/menu")



