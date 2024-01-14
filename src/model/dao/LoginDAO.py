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

        
    def add_new_admin(self, username, password):
            try:
                self.db.open_connection()

                # Check if the username exists in the database
                query = "SELECT administradorID, Password FROM Adminstrators WHERE Username = ?"
                self.db.cursor.execute(query, (username,))
                result = self.db.cursor.fetchone()

                if result:
                    admin_id = result[0]
                    stored_password_hash = result[1]

                    if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
                        # Correct username, correct password
                        return admin_id
                    else:
                        # Incorrect password
                        return 0
                else:
                    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    insert_query = "INSERT INTO Administrators (Username, Password) VALUES (?, ?)"
                    self.db.cursor.execute(insert_query, (username, hashed_password))
                    self.db.connection.commit()

                    # Retrieve the client ID of the newly inserted record
                    self.db.cursor.execute("SELECT last_insert_rowid()")
                    admin_id = self.db.cursor.fetchone()[0]

                    return admin_id  # new client

            except sqlite3.Error as error:
                print("Error while checking username existence or adding new admin", error)
            finally:
                self.db.close_connection()
                print("The SQLite connection is closed")

