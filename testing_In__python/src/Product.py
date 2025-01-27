from testing_In__python.src.ProductUnit import ProductUnit

class Product:
    def __init__(self, name: str, unit: ProductUnit, price: float):
        self.name = name
        self.unit = unit
        self.price = price  # Add the price attribute here

    def set_price(self, price: float):
        self.price = price
