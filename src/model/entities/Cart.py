class Cart:
    def __init__(self):
        self.items = []

    def addProduct(self, product, quantity=1):
        for item in self.items:
            if item['product'].getID() == product.getID():
                item['quantity'] += quantity
                return

        self.items.append({'product': product, 'quantity': quantity})

    def removeProduct(self, product_id):
        self.items = [item for item in self.items if item['product'].getID() != product_id]

    def getCartItems(self):
      
        return self.items
    def getTotal(self):

        total = 0.0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total

    def clearCart(self):

        self.items = []