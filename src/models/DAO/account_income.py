from sqlalchemy import (Column, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Definição da classe Base
Base = declarative_base()

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nome = Column(String, nullable=False)

class ConnectionClass:
    def __init__(self, file_db):
        self.file_db = file_db
        self.engine = None
        self.Session = None

    def connect(self):
        try:
            # Criando o engine
            self.engine = create_engine(self.file_db)
            self.Session = sessionmaker(bind=self.engine)
            # Criar tabelas aqui
            Base.metadata.create_all(self.engine)
            print(f"Conexão estabelecida com {self.file_db}!")
        except Exception as e:
            print(f"Erro ao conectar-se ao banco de dados: {e}")

    def get_session(self):
        if not self.Session:
            raise Exception("A conexão com o banco de dados não foi estabelecida.")
        return self.Session()

def connect():
    conn = ConnectionClass("sqlite:///financas.db")
    conn.connect()  # Chamar o método de conexão aqui
    return conn

def addAccount(nome):
    session = connect().get_session()
    try:
        newAccount = Account(nome=nome)
        session.add(newAccount)
        session.commit()
        print(f"Conta '{nome}' adicionada com sucesso.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao criar a conta: {e}")
# Função para ler todas as contas
def read_all_account():
    session = connect().get_session()
    try:
        accounts = session.query(Account).all()
        return accounts
    except SQLAlchemyError as e:
        print(f"Erro ao ler as contas: {e}")

# Função para ler uma conta por ID
def read_account_by_id(id):
    session = connect().get_session()
    try:
        account = session.query(Account).filter_by(id=id).first()
        return account
    except SQLAlchemyError as e:
        print(f"Erro ao ler a conta: {e}")

# Função para deletar uma conta por ID
def delete_account(id):
    session = connect().get_session()
    try:
        account = session.query(Account).filter_by(id=id).first()
        if account:
            session.delete(account)
            session.commit()
            print(f"Conta com ID {id} deletada com sucesso.")
        else:
            print(f"Conta com ID {id} não encontrada.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao deletar a conta: {e}")

# Função para atualizar o nome de uma conta por ID
def update_account(id, nome):
    session = connect().get_session()
    try:
        account = session.query(Account).filter_by(id=id).first()
        if account:
            if nome:
                account.nome = nome
                session.commit()
                print(f"Conta com ID {id} atualizada com sucesso.")
            else:
                print("Nenhum nome fornecido para atualização.")
        else:
            print(f"Conta com ID {id} não encontrada.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro ao atualizar a conta: {e}")

# Execução principal
if __name__ == '__main__':
    # addAccount("Banco RICO")


    # for contas in read_all_account():
    #     print(contas.id, contas.nome)


    # print(read_account_by_id(2).nome)

    # delete_account(2)
    pass
    update_account(1,"Votorantin")

    for contas in read_all_account():
        print(contas.id, contas.nome)