from model.dto.AdminDTO import AdminDTO
from model.services.ConnectionService import Connection
import sqlite3
import os
import bcrypt

current_dir = os.getcwd()

class LoginDao:

    def __init__(self):
        
        # Defines the relative path to our database file
        db_relative_path = os.path.join('db', 'Kitchen_database')
        
        self.db = Connection(db_relative_path)

    def check_username_existence(self, username):
        try:
            self.db.open_connection()

            query = "SELECT username, password FROM Administrators WHERE username = ?"
            self.db.cursor.execute(query, (username,))
            result = self.db.cursor.fetchone()

            if result:
                admin_service = AdminDTO(username=result[0], password=result[1])
                return admin_service
            else:
                return None

        except sqlite3.Error as error:
            print("Error while checking username existence", error)
        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")

    def add_new_user(self, username, password):
        try:
            self.db.open_connection()

            # Encode and hash the password
            password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

            # Prepare the insert query
            query = "INSERT INTO Administrators (username, password) VALUES (?, ?)"

            # Execute the query
            self.db.cursor.execute(query, (username, hashed_password))

            # Commit the changes
            self.db.connection.commit()

            print("New user added successfully")

        except sqlite3.Error as error:
            print("Error while adding new user", error)

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")

