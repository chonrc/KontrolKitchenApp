from model.services.ConnectionService import Connection
import sqlite3
import os
from model.entities.Product import Product

current_dir = os.getcwd()

class ProductDAO:

    def __init__(self):
        
        db_relative_path = os.path.join('db', 'Kitchen_database')
        self.db = Connection(db_relative_path)


    def add_new_Product(self, name, description, price, image):
        try:
            self.db.open_connection()

            query = "INSERT INTO Products (name, description, price, quantity, image) VALUES (?, ?, ?, 1, ?)"

            self.db.cursor.execute(query, (name, description , price, image))

            self.db.connection.commit()

            print("New Product added successfully")

        except sqlite3.Error as error:
            print("Error while adding new Product", error)

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")

    def getAllProducts(self):
        try:
            self.db.open_connection()

            query = "SELECT * FROM Products"
            self.db.cursor.execute(query)

            products_data = self.db.cursor.fetchall()

            products_list = []
            for product_data in products_data:
                product = Product(*product_data)
                products_list.append(product)
                
            return products_list

        except sqlite3.Error as error:
            print("Error while fetching all products", error)
            return []

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")
