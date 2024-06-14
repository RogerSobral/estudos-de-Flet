from sqlite3 import connect
from typing import List
class AccountIncomeModel:

    def __init__(self,db_file):
        self.connection = connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                 CREATE TABLE IF NOT EXISTS  account_income(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL DEFAULT 'Carteira'
                );
                """)
        self.connection.commit()

    def addCategory(self, name) -> None:
        self.newConnect()
        try:
            self.cursor.execute("""
                                INSERT INTO account_income(name)
                                VALUES(?)

                               """, (name,))
            self.connection.commit()
        except Exception as e:
            print("Essa Conta já existe ")
        finally:
            self.closeConnection()

    def selectCategorys(self) -> List:
        self.newConnect()
        self.cursor.execute("""
                            SELECT * FROM account_income
                           ;
                           """)
        lista = self.cursor.fetchall()
        self.closeConnection()
        return lista

    def selectSingleCategory(self, name):
        self.newConnect()
        self.cursor.execute("""
                                   SELECT * FROM account_income
                                   WHERE name LIKE ?
                                  """, (name,))
        category = self.cursor.fetchone()
        self.closeConnection()
        return category

    def deleteCategoryID(self, id) -> None:
        self.newConnect()
        self.cursor.execute("""
                                          DELETE FROM account_income
                                          where id = ?
                                         ;
                                         """, (id,))
        self.connection.commit()
        self.closeConnection()
        print("Categoria deletada com sucesso !")

    def deleteCategoryName(self, name) -> None:
        self.newConnect()
        self.cursor.execute("""
                                          DELETE FROM account_income
                                          where name LIKE ?
                                         """, (name,))
        self.connection.commit()
        self.closeConnection()
        print("Deletado com sucesso ! ")

    def UpdateCategory(self, name, id) -> None:
        self.newConnect()
        self.cursor.execute("""
                                          UPDATE account_income 
                                          SET name= ? 
                                          where id = ?

                                         """, (name, id))
        self.connection.commit()
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


