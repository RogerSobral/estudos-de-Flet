from sqlite3 import connect

class CategoryIncomeModel:

    def __init__(self,db_file):
        self.connection = connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                 CREATE TABLE IF NOT EXISTS  category_income(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL DEFAULT 'Salario'
                );
                """)
        self.connection.commit()
