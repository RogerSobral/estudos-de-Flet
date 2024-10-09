from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from src.DAO.conn import ConnectionClass
import bcrypt

Base=declarative_base()

class UserModal(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    senha = Column(String)

    def set_senha(self, senha):
        # Gera o salt e faz o hash da senha
        salt = bcrypt.gensalt()
        self.senha = bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')

        # Método para verificar a senha

    def check_senha(self, senha):
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha.encode('utf-8'))



if __name__ == '__main__':

    conn = ConnectionClass('sqlite:///financas.db')
    conn.connect()

    # Obtém a sessão para interagir com o banco de dados
    session = conn.get_session()

    # Cria as tabelas no banco de dados
    Base.metadata.create_all(conn.engine)

    # Exemplo de inserção de um novo usuário
    # novo_usuario = User(nome='maria', senha="so1234")
    # session.add(novo_usuario)
    # session.commit()  # Salva a transação no banco de dados
    # print("Usuário adicionado com sucesso!")

    # Exemplo de consulta
    usuarios = session.query(UserModal).all()
    for usuario in usuarios:
        print(f'ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.senha}')
