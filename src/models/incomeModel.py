from sqlite3 import connect

class IncomeModel:

    def __init__(self,db_file):
        self.db_file=db_file
        self.connection = connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
         CREATE TABLE IF NOT EXISTS  income(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         description TEXT NOT NULL,
         id_category INTEGER DEFAULT 1 ,
       
         FOREIGN KEY (id_category) REFERENCES category_income (id)
        );
        """)
        self.connection.commit()

    def addCategory(self, name) -> None:
        self.newConnect()
        try:
            self.cursor.execute("""
                             INSERT INTO category_income(name)
                             VALUES(?)

                            """, (name,))
            self.connection.commit()
        except Exception as e:
            print("Essa Categoria já existe ")
        finally:
            self.closeConnection()

    def newConnect(self) -> None:
        try:
            self.connection = connect(self.db_file)
            self.cursor = self.connection.cursor()

        except Exception as e:
            print(f"Erro {e}")

    def closeConnection(self) -> None:
        """
        This is method close the db
        :paramater
        :return: None
        """
        self.cursor.close()
        self.connection.close()
