from model.services.AdminService import AdminService
from model.services.ConnectionService import Connection
import sqlite3

class AdminDao:
    def __init__(self):
        self.db = Connection('db/Kitchen_database')

    def check_username_existence(self, username):
        try:
            self.db.open_connection()

            query = "SELECT username, password FROM Administrators WHERE username = ?"
            self.db.cursor.execute(query, (username,))
            result = self.db.cursor.fetchone()

            if result:
                # If the username exists, create an AdminService object
                admin_service = AdminService(username=result[0], password=result[1])
                return admin_service
            else:
                return None

        except sqlite3.Error as error:
            print("Error while checking username existence", error)
        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")
