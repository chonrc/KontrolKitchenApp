import os
from fpdf import FPDF
import webbrowser
from model.entities.Client import Client



class Cart:

    client_dto = None

    def __init__(self):
        self.items = []
        



    def getClient(self):
        return self.client_dto 
    
    def setClient(self, client):
        self.client_dto = client
    
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
            total += item['product'].getPrice() * item['quantity']
        return total

    def clearCart(self):
        self.items = []

    def receipt(self):
        
        pdf = FPDF()
        pdf.add_page()

        # Set the right margin to be the same as the left margin
        pdf.r_margin = pdf.l_margin

       

        pdf.set_fill_color(200, 200, 200)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", 'B', size = 15)
        pdf.cell(0, 10, txt = "Receipt", border = 1, fill = True, ln = 1, align = 'C')

        pdf.set_font("Arial", size = 12)
        for item in self.items:
            product = item['product']
            quantity = item['quantity']
            pdf.cell(0, 10, txt = f"Product Name: {product.getName()}, Quantity: {quantity}, Price: {product.getPrice()}", border = 1, fill = True, ln = 1, align = 'L')

        pdf.ln(10)

        pdf.set_font("Arial", 'B', size = 15)
        pdf.cell(0, 20, txt = f"Total: {self.getTotal()}", border = 1, fill = True, ln = 2, align = 'C')

        pdf.image('src/view/resources/logo_negro.png', x = 170, y = 10, w = 30)

        pdf_file = "receipt.pdf"
        pdf.output(pdf_file)

        webbrowser.open_new(r'file://' + os.path.realpath(pdf_file))
