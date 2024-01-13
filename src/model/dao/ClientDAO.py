from model.services.ConnectionService import Connection
import sqlite3
import os
import bcrypt

current_dir = os.getcwd()

class ClientDao:

    def __init__(self):
        
        db_relative_path = os.path.join('db', 'Kitchen_database')
        
        self.db = Connection(db_relative_path)

    def check_username_existence(self, username, password):
        try:
            self.db.open_connection()

            # Check if the username exists in the database
            query = "SELECT Username, Password FROM Clients WHERE Username = ?"
            self.db.cursor.execute(query, (username,))
            result = self.db.cursor.fetchone()

            if result:
                stored_password_hash = result[1]
                if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
                    #correct username, correct password 
                    return 1
                else:
                    #Incorrect password 
                    return 0
            else:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                insert_query = "INSERT INTO Clients (Username, Password) VALUES (?, ?)"
                self.db.cursor.execute(insert_query, (username, hashed_password))
                self.db.connection.commit()
                return 2    #new client

        except sqlite3.Error as error:
            print("Error while checking username existence or adding new client", error)
        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")

    
    
    def get_number_of_clients(self):
        try:
            self.db.open_connection()

            query = "SELECT COUNT(*) FROM Clients"
            self.db.cursor.execute(query)

            num_clients = self.db.cursor.fetchone()[0]

            return num_clients

        except sqlite3.Error as error:
            print("Error while getting the number of Clients", error)
            return -1  

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")
