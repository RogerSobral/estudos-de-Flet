from sqlite3 import connect
from src.models.entity.user import User
import os
import sys
import sqlite3


class UserModel:

    def __init__(self):
        self.db_file="dao/controleFinanceiro.db"
        # self.connection = connect("dao/controleFinanceiro.db")
        # self.cursor = self.connection.cursor()
        self.create_table()

    def create_connection(self):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # Change the db_file to the absolute path
            db_file = os.path.join(sys._MEIPASS, self.db_file)
        else:
            db_file=self.db_file

        connection = sqlite3.connect(db_file)
        connection.row_factory = sqlite3.Row
        connection.enable_load_extension(True)
        sqlite_vss.load(connection)
        connection.enable_load_extension(False)
        return connection


    def create_table(self):
        self.cursor.execute("""
                 CREATE TABLE IF NOT EXISTS  users(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 login TEXT NOT NULL,
                 password TEXT NOT NULL
                );
                """)
        self.connection.commit()




    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)",
                            (user.login, user.password))
        self.connection.commit()

    def get_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        lista=self.cursor.fetchall()
        return lista

    def update_user(self, user_id, login, password):
        self.cursor.execute("UPDATE users SET username = ?, email = ? WHERE id = ?",
                            (login, password, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()



if __name__ == '__main__':

    u1=UserModel()
    log1=User("pedro","3333")
    u1.add_user(log1)