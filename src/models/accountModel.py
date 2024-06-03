from sqlite3 import connect

class AccountIncomeModel:

    def __init__(self,db_file):
        self.connection = connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                 CREATE TABLE IF NOT EXISTS  account_income(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL DEFAULT 'Carteira'
                );
                """)
        self.connection.commit()
