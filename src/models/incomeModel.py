from sqlite3 import connect

class IncomeModel:

    def __init__(self,db_file):
        self.connection = connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
         CREATE TABLE IF NOT EXISTS  income(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         description TEXT NOT NULL,
         value_income REAL NOT NULL,
         installment integer,
         due_date TEXT,
         status INTEGER,
         id_category INTEGER DEFAULT 1 ,
         id_account INTEGER DEFAULT 1,
         FOREIGN KEY (id_category) REFERENCES category_income (id)
         FOREIGN KEY (id_account) REFERENCES account_income (id)
        );
        """)
        self.connection.commit()