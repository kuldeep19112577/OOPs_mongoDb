from pymongo import MongoClient


class Product:

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:

    def __init__(self):

        connection_string = "mongodb+srv://Nexturn_DB20:DjhEobMBQ0rGMW69@cluster0.xnuhy3x.mongodb.net/?appName=Cluster0"

        self.mongo_client = MongoClient(connection_string)
        self.database = self.mongo_client["shoppingcart"]

        self.products = self.database["products"]
        self.cart = self.database["cart"]

    def add_product(self, product):

        data = {
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        }

        self.cart.insert_one(data)

    def remove_product(self, product_name):

        self.cart.delete_one({
            "name": product_name
        })

    def calculate_total(self):

        total = 0
        cart = self.cart.find()

        for i in cart:
            total += i["price"] * i["quantity"]

        return total


P1 = Product("laptop", 1000, 1)
p2=Product("mouse",500,4)
c1 = Cart()

# c1.add_product(P1)
c1.add_product(p2)




print(c1.calculate_total())