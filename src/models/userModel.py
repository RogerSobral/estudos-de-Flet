from sqlite3 import connect

class UserModel:

    def __init__(self,db_file):
        self.connection = connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

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
        return self.cursor.fetchall()

    def update_user(self, user_id, login, password):
        self.cursor.execute("UPDATE users SET username = ?, email = ? WHERE id = ?",
                            (login, password, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()



