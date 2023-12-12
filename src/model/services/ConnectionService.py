import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def open_connection(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()
