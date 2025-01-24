from unit_test_project.src.Product import Product

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item_quantity(self, product: Product, quantity: float):
        # Store the product, quantity, and price of the product
        self.items[product.name] = {
            'product': product,
            'quantity': quantity,
            'price': product.price  # Assuming 'product' has a 'price' attribute
        }
