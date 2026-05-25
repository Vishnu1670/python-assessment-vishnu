#importing the abstractmethod
from abc import ABC, abstractmethod
from datetime import date, timedelta


#abstract Base Class
class Product(ABC):

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    @abstractmethod
    def final_price(self):
        pass


# Electronics Class
class Electronics(Product):

    def __init__(self, product_id, name, price, warranty_months):
        super().__init__(product_id, name, price)
        self.warranty_months = warranty_months

    def final_price(self):
        #calculate the gst for the given product
        gst = self.price * 0.18
        return self.price + gst


# Clothing Class
class Clothing(Product):

    def __init__(self, product_id, name, price, size, fabric):
        super().__init__(product_id, name, price)
        self.size = size
        self.fabric = fabric

    def final_price(self):
        gst = self.price * 0.05
        return self.price + gst


# Grocery Class
class Grocery(Product):

    def __init__(self, product_id, name, price, expiry):
        super().__init__(product_id, name, price)
        self.expiry = expiry

    def final_price(self):

        days_left = (self.expiry - date.today()).days

        #apply 30% discount if expiry within 7 days
        if days_left <= 7:
            discount = self.price * 0.30
            return self.price - discount

        return self.price


# Cart Class
class Cart:

    def __init__(self, customer):
        self.customer = customer
        self.items = []

    # Add item to cart
    def add_item(self, product, qty):
        self.items.append((product, qty))

    # Remove item using product id
    def remove_item(self, product_id):

        for item in self.items:
            product, qty = item

            if product.product_id == product_id:
                self.items.remove(item)
                print(f"{product.name} removed from cart")
                return

        print("Product not found")

    #print invoice
    def print_invoice(self):
        #chat GPT idea
        print("\n===== SHOPSMART INVOICE =====")
        print("Customer:", self.customer)
        print("-" * 50)

        grand_total = 0

        print(f"{'Item':15} {'Qty':5} {'Unit Price':12} {'Line Total'}")
        print("-" * 50)

        for product, qty in self.items:

            unit_price = product.final_price()
            line_total = unit_price * qty

            grand_total += line_total

            print(
                f"{product.name:15} {qty:<5} "
                f"{unit_price:<12.2f} {line_total:.2f}"
            )

        print("-" * 50)
        print(f"Grand Total: {grand_total:.2f}")


cart = Cart(customer="Divya")

cart.add_item(Electronics("E01","Headphones",2000,warranty_months=12),qty=1)

cart.add_item(Clothing("C01","Cotton Shirt",800,size="M",fabric="Cotton"),qty=2)

cart.add_item(Grocery("G01","Milk",60,expiry=date.today() + timedelta(days=3)),qty=4 )
cart.remove_item("E01")
cart.remove_item("E01")
cart.print_invoice()