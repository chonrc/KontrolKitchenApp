from model.services.ConnectionService import Connection
import sqlite3
import os
from model.entities.Product import Product
from model.dto.ProductDTO import ProductDTO
current_dir = os.getcwd()

class ProductDAO:

    def __init__(self):
        
        db_relative_path = os.path.join('db', 'Kitchen_database')
        self.db = Connection(db_relative_path)

    def get_products_dto(self):
        try:
            self.db.open_connection()

            query = "SELECT name, quantity FROM Products"
            self.db.cursor.execute(query)

            products_data = self.db.cursor.fetchall()

            products_dto_list = []
            for product_data in products_data:
                product_dto = ProductDTO(name=product_data[0], quantity=product_data[1])
                products_dto_list.append(product_dto)

            return products_dto_list

        except sqlite3.Error as error:
            print("Error while fetching product DTOs", error)
            return []

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")

            
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
            
    def get_number_of_products(self):
        try:
            self.db.open_connection()

            query = "SELECT COUNT(*) FROM Products"
            self.db.cursor.execute(query)

            num_products = self.db.cursor.fetchone()[0]

            return num_products

        except sqlite3.Error as error:
            print("Error while getting the number of products", error)
            return -1  

        finally:
            self.db.close_connection()
            print("The SQLite connection is closed")