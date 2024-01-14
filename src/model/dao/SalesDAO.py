from model.services.ConnectionService import Connection
import sqlite3
import os
import bcrypt

current_dir = os.getcwd()

class SalesDAO:
    def __init__(self):
        db_relative_path = os.path.join('db', 'Kitchen_database')
        self.db = Connection(db_relative_path)

    def get_number_of_sales(self):
        try:
            self.db.open_connection()

            query = "SELECT COUNT(*) FROM Sales"
            self.db.cursor.execute(query)

            num_clients = self.db.cursor.fetchone()[0]

            return num_clients

        except sqlite3.Error as error:
            print("Error while getting the number of Sales", error)
            return -1  

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")


    def get_total_benefit(self):
        try:
            self.db.open_connection()

            query = "SELECT SUM(Total) FROM Sales"
            self.db.cursor.execute(query)

            total_benefit = self.db.cursor.fetchone()[0]

            # If there are no sales yet, return 0
            return total_benefit if total_benefit is not None else 0

        except sqlite3.Error as error:
            print("Error while getting the total benefit", error)
            return -1

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")