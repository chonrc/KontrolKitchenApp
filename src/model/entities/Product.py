class Product:
    def __init__(self, product_id, name, description, price, quantity, image):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.image = image

    def getID(self):
        return self.product_id

