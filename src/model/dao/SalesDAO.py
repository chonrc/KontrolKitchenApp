from model.services.ConnectionService import Connection
import sqlite3
import os
import bcrypt
from datetime import datetime

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


    def add_sale(self, client_id, total, table_number, products):
        try:
            self.db.open_connection()

            # Get the current date and time in the format 'YYYY-MM-DD HH:MM:SS'
            sale_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Insert into "Sales" table
            sale_query = "INSERT INTO Sales (ClientID, Total, SaleDate, TableNumber) VALUES (?, ?, ?, ?)"
            sale_values = (client_id, total, sale_date, table_number)

            self.db.cursor.execute(sale_query, sale_values)
            sale_id = self.db.cursor.lastrowid

            # Insert or update into "SaleProducts" table
            if products:
                product_query = "INSERT OR REPLACE INTO SaleProducts (SaleID, ProductID, Quantity) VALUES (?, ?, ?)"
                product_values = [(sale_id, product_id, quantity) for product_id, quantity in products]

                self.db.cursor.executemany(product_query, product_values)

            self.db.connection.commit()

            return sale_id

        except sqlite3.Error as error:
            print("Error while adding a new sale", error)
            return -1

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")
