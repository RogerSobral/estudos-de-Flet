from sqlite3 import connect
from src.models.entity.user import User
import os
import sys
import sqlite3


class UserModel:

    def __init__(self):
        self.connection = connect(self.create_path(),check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_path(self):
        caminho_do_arquivo = "dao/controleFinanceiro.db"
        caminho_absoluto = os.path.abspath(caminho_do_arquivo)
        diretorio = os.path.dirname(caminho_absoluto)
        return diretorio


    def create_table(self):
        self.cursor.execute("""
                 CREATE TABLE IF NOT EXISTS  users(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 login TEXT NOT NULL,
                 password TEXT NOT NULL
                );
                """)
        self.connection.commit()




    def add_user(self, user:User):
        self.cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)",
                            (user.login, user.password))
        self.connection.commit()



    def get_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")

        lista=self.cursor.fetchall()
        print(lista)
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