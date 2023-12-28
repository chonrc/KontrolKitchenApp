import sqlite3

class Connection:
    _instance = None

    def __new__(cls, db_name):
        if not cls._instance:
            cls._instance = super(Connection, cls).__new__(cls)
            cls._instance.db_name = db_name
            cls._instance.connection = None
            cls._instance.cursor = None
        return cls._instance

    def open_connection(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()

    def close_connection(self):
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None
