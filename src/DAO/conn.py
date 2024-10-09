from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ConnectionClass:
    def __init__(self,file_db):
        self.file_db=file_db
        self.engine = None
        self.Session = None

    def connect(self):
        try:
            self.engine = create_engine(self.file_db)
            self.Session = sessionmaker(bind=self.engine)
            with self.engine.connect() as connection:
                print(f"Conexão estabelecida com {self.file_db}!")
        except Exception as e:
            print(f"Erro ao conectar-se ao banco de dados: {e}")

    def get_session(self):
        if not self.Session:
            raise Exception("A conexão com o banco de dados não foi estabelecida.")
        return self.Session()


