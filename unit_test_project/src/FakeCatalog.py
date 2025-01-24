class FakeCatalog:
    def __init__(self):
        self.products = {}

    def add_product(self, product, price):
        self.products[product.name] = price

    def get_product(self, name):
        return self.products.get(name)