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
            query = "SELECT ClientID, Password FROM Clients WHERE Username = ?"
            self.db.cursor.execute(query, (username,))
            result = self.db.cursor.fetchone()

            if result:
                client_id = result[0]
                stored_password_hash = result[1]

                if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
                    # Correct username, correct password
                    return client_id
                else:
                    # Incorrect password
                    return 0
            else:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                insert_query = "INSERT INTO Clients (Username, Password) VALUES (?, ?)"
                self.db.cursor.execute(insert_query, (username, hashed_password))
                self.db.connection.commit()

                # Retrieve the client ID of the newly inserted record
                self.db.cursor.execute("SELECT last_insert_rowid()")
                client_id = self.db.cursor.fetchone()[0]

                return client_id  # new client

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


            
    def get_clients_list(self):
        try:
            self.db.open_connection()

            query = "SELECT Username, ClientID FROM Clients"
            self.db.cursor.execute(query)

            clients_list = self.db.cursor.fetchall()

            return clients_list

        except sqlite3.Error as error:
            print("Error while getting the list of Clients", error)
            return None  

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")

    def get_clients_sales_summary(self):
        try:
            self.db.open_connection()

            query = """
                SELECT C.ClientID, C.Username, SUM(S.Total) as TotalSales
                FROM Clients C
                LEFT JOIN Sales S ON C.ClientID = S.ClientID
                GROUP BY C.ClientID, C.Username
            """
            self.db.cursor.execute(query)

            clients_sales_data = self.db.cursor.fetchall()

            clients_sales_summary_list = []
            for client_sales_data in clients_sales_data:
                client_sales_summary = {
                    'ClientID': client_sales_data[0],
                    'Username': client_sales_data[1],
                    'TotalSales': client_sales_data[2]
                }
                clients_sales_summary_list.append(client_sales_summary)

            return clients_sales_summary_list

        except sqlite3.Error as error:
            print("Error while fetching clients' sales summary", error)
            return []

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")