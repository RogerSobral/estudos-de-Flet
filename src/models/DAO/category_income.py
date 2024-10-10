from sqlalchemy import (Column, Integer, String,create_engine)
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy.exc import SQLAlchemyError
Base=declarative_base()
class Category(Base):
    __tablename__ ="category"
    id= Column(Integer ,primary_key=True, autoincrement=True, unique=True)
    nome =Column(String)

class ConnectionClass:
    def __init__(self, file_bd):
        self.file_db=file_bd
        self.engine=None
        self.Session=None

    def connect (self):
        try:
            self.engine=create_engine(self.engine)
            self.Session=sessionmaker(bind=self.engine)
            Base.metadata.create_all(self.engine)
            print(f"Conexão estabelecida com {self.file_db}!")
        except Exception as e:
            print(f"Erro ao conectar-se ao banco de dados: {e}")


    def get_session(self):
        if not self.Session:
            raise Exception("A conexão com o banco de dados não foi estabelecida.")
        return self.Session()


def connect():
    # Ela vai gerar o Objeto de connection e uma connect e retornar conn
    conn=ConnectionClass("sqlite:///financas.db")
    conn.connect()
    return conn


def addCategory(nome):
    session=connect().get_session()
    try:
        # Crio um objeto do tipo category
        category=Category(nome)
        # inicio a transação de envio do atributo em formato de entidade categoria
        session.add(category)
        # dou um commit para implementar a mudança
        session.commit()
        print(f"Categoria {nome} adicionada com sucesso!")
    except SQLAlchemyError as e:
        print(f"Erro ao criar a categoria: {e}")
        # Ele vai impedir retornar o estado antes da session, para impedir inconsistência
        session.rollback()

