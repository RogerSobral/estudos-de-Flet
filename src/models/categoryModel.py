from sqlite3 import connect
from typing import List
class CategoryIncomeModel:

    def __init__(self,db_file):
        self.db_file=db_file
        self.connection:connect = None
        self.cursor = None
        self.newConnect()
        self.create_table()

    def create_table(self) -> None:
        self.newConnect()
        self.cursor.execute("""
                 CREATE TABLE IF NOT EXISTS  category_income(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL UNIQUE DEFAULT 'SALARIO'
                );
                """)
        self.connection.commit()
        self.closeConnection()

    def addCategory(self, name) -> None:
        self.newConnect()
        try:
            self.cursor.execute("""
                             INSERT INTO category_income(name)
                             VALUES(?)
                            
                            """,(name,))
            self.connection.commit()
        except Exception as e:
            print("Essa Categoria já existe ")
        finally:
            self.closeConnection()

    def selectCategorys(self)-> List:
        self.newConnect()
        self.cursor.execute("""
                         SELECT * FROM category_income
                        ;
                        """)
        lista=self.cursor.fetchall()
        self.closeConnection()
        return lista


    def selectSingleCategory(self, name):
        self.newConnect()
        self.cursor.execute("""
                                SELECT * FROM category_income
                                WHERE name LIKE ?
                               """,(name,))
        category = self.cursor.fetchone()
        self.closeConnection()
        return category


    def deleteCategoryID(self,id) -> None:
        self.newConnect()
        self.cursor.execute("""
                                       DELETE FROM category_income
                                       where id = ?
                                      ;
                                      """, (id,))
        self.connection.commit()
        self.closeConnection()
        print("Categoria deletada com sucesso !")

    def deleteCategoryName(self,name) -> None:
        self.newConnect()
        self.cursor.execute("""
                                       DELETE FROM category_income
                                       where name LIKE ?
                                      """, (name,))
        self.connection.commit()
        self.closeConnection()
        print("Deletado com sucesso ! ")

    def UpdateCategory(self,name,id) -> None:
        self.newConnect()
        self.cursor.execute("""
                                       UPDATE category_income 
                                       SET name= ? 
                                       where id = ?
                                      
                                      """, (name,id))
        self.connection.commit()
        self.closeConnection()

    def newConnect(self)->None:
        try:
            self.connection = connect(self.db_file)
            self.cursor = self.connection.cursor()

        except Exception as e:
            print(f"Erro {e}")


    def closeConnection(self)->None:
        """
        This is method close the db
        :paramater
        :return: None
        """
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    banco=CategoryIncomeModel("fincancas.db")
    print(banco.selectCategorys())
    print(banco.selectSingleCategory("MENTORIA"))
    banco.deleteCategoryID(2)
    print(banco.selectCategorys())

