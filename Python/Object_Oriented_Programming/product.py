class Products(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.tax = .15
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(tax):
        return self.price * (1 + tax)
    def returns(self, reason):
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        if self.reason == "in box":
            self.status = "for sale"
            self.price = 0
        if self.reason == "opened":
            self.status = "used"
            self.price = price * .80
        return self
    def displayInfo(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self
