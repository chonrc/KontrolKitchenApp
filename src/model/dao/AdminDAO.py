from model.services.AdminService import AdminService
from model.services.ConnectionService import Connection
import sqlite3
import os

# At the start of your script
import os

# Get the current working directory
current_dir = os.getcwd()

# Define the relative path to your project directory
#project_relative_path = os.path.join(current_dir, '..')

# Change the working directory to the project directory
#os.chdir(project_relative_path)

print("Current working directory is now: ", os.getcwd())

class AdminDao:

    def __init__(self):
        
        # Define the relative path to your database file
        db_relative_path = os.path.join('db', 'Kitchen_database')

        print("Database file is located here: ", db_relative_path)
        
        self.db = Connection(db_relative_path)

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
