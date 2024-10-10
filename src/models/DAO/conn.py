from sqlalchemy import (Column, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError


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
            Base.metadata.create_all(self.engine)  # Criar tabelas aqui
            print(f"Conexão estabelecida com {self.file_db}!")
        except Exception as e:
            print(f"Erro ao conectar-se ao banco de dados: {e}")

    def get_session(self):
        if not self.Session:
            raise Exception("A conexão com o banco de dados não foi estabelecida.")
        return self.Session()



