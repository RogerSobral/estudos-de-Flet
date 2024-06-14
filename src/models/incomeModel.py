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

    def addCategory(self, description,id_category) -> None:
        self.newConnect()
        try:
            self.cursor.execute("""
                             INSERT INTO income(description,id_category)
                             VALUES(?,?)
                            """, (description,id_category))
            self.connection.commit()
        except Exception as e:
            print("Essa Receita já existe ")
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

    def listIncome(self):
        self.newConnect()
        self.cursor.execute("""
                                 SELECT * FROM income
                                ;
                                """)
        lista = self.cursor.fetchall()
        self.closeConnection()
        return lista


    def listIncomeSigle(self,description):
        self.newConnect()
        self.cursor.execute("""
                                        SELECT * FROM income
                                        WHERE description LIKE ?
                                       """, (description,))
        category = self.cursor.fetchone()
        self.closeConnection()
        return category


    def deleteIncomeID(self,id) -> None:
        self.newConnect()
        self.cursor.execute("""
                                       DELETE FROM income
                                       where id = ?
                                      ;
                                      """, (id,))
        self.connection.commit()
        self.closeConnection()
        print("Receita deletada com sucesso !")



    def deleteIncomeName(self,description) -> None:
        self.newConnect()
        self.cursor.execute("""
                                       DELETE FROM income
                                       where description LIKE ?
                                      """, (description,))
        self.connection.commit()
        self.closeConnection()
        print("Deletado com sucesso ! ")



    def UpdateIncome(self, description, id) -> None:
        self.newConnect()
        self.cursor.execute("""
                                       UPDATE income 
                                       SET description= ? 
                                       where id = ?

                                      """, (description, id))
        self.connection.commit()
        self.closeConnection()

