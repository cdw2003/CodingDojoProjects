from product import Products
class Store(object):
    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
        self.products = [product1, product2, product3, product4, product5, product6]
    def add_product(self, products):
        self.products.append(products)
        return self
    def remove_product(self, products):
        self.products.remove(products)
        return self
    def inventory(self):
        for product in self.products:
            print product.item_name
            print product.price
            print product.weight
            print product.brand
            print product.cost
            print product.status
        return self

product1 = Products(1.25, "apples", ".15lb", "Gala", .50, "for sale")
product2 = Products(1.50, "bananas", ".25lb", "Chiquita", .75, "for sale")
product3 = Products(0.85, "carrots", ".28lb", "Bolthouse Farms", .21, "for sale")
product4 = Products(0.65, "spinach", ".32lb", "Dole", .35, "for sale")
product5 = Products(0.79, "kale", ".36lb", "Earthbound Farm", .28, "for sale")
product6 = Products(0.55, "grapefruit", ".18lb", "Wonderful Citrus", .18, "for sale")
product7 = Products(2.50, "ice cream", ".92lb", "Breyer's", .75, "for sale")
store1 = Store("Virginia", "Mrs. C")
store1.add_product(product7)
store1.remove_product(product6)
store1.inventory()
