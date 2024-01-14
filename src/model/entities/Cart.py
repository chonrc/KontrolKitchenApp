import os
from fpdf import FPDF
import webbrowser
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
            total += item['product'].getPrice() * item['quantity']
        return total

    def clearCart(self):
        self.items = []

    def receipt(self):
        
        pdf = FPDF()
        pdf.add_page()

        # Set the right margin to be the same as the left margin
        pdf.r_margin = pdf.l_margin

       

        # Set the fill color to light gray
        pdf.set_fill_color(200, 200, 200)
        # Set the text color to black
        pdf.set_text_color(0, 0, 0)
        # Set the font to Arial, bold, size 15
        pdf.set_font("Arial", 'B', size = 15)
        # Create a cell with a border, a background color, and a centered text
        pdf.cell(0, 10, txt = "Receipt", border = 1, fill = True, ln = 1, align = 'C')

        # Add the items and their quantities to the receipt
        pdf.set_font("Arial", size = 12)
        for item in self.items:
            product = item['product']
            quantity = item['quantity']
            pdf.cell(0, 10, txt = f"Product Name: {product.getName()}, Quantity: {quantity}, Price: {product.getPrice()}", border = 1, fill = True, ln = 1, align = 'L')

        # Add an empty line
        pdf.ln(10)

        # Add the total to the receipt
        pdf.set_font("Arial", 'B', size = 15)
        pdf.cell(0, 20, txt = f"Total: {self.getTotal()}", border = 1, fill = True, ln = 2, align = 'C')

         # Add an image to the receipt (replace 'path_to_image.jpg' with your image file path)
        pdf.image('src\\view\\resources\\logo_negro.png', x = 170, y = 10, w = 30)

        # Save the receipt as a PDF
        pdf_file = "receipt.pdf"
        pdf.output(pdf_file)

        # Open the PDF file
        webbrowser.open_new(r'file://' + os.path.realpath(pdf_file))
