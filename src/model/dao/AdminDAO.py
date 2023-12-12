import sqlite3
from model.services.AdminService import AdminService

class AdminDao:
    def check_username_existence(self, username):
        try:
            sqliteConnection = sqlite3.connect('db/Kitchen_database')
            cursor = sqliteConnection.cursor()

            query = "SELECT username, password FROM Administrators WHERE username = ?"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                # If the username exists, create an AdminService object
                admin_service = AdminService(username=result[0], password=result[1])
                return admin_service
            else:
                return None

        except sqlite3.Error as error:
            print("Error while checking username existence", error)
        finally:
            if 'sqliteConnection' in locals():
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def close_connection(self):
        self.connection.close()
