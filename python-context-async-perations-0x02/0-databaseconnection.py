import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn  # gives connection back to use inside 'with'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()  # always closes connection





#with DatabaseConnection("my_database.db") as conn:
 #   cursor = conn.cursor()
  #  cursor.execute("SELECT * FROM users")
   # print(cursor.fetchall())
