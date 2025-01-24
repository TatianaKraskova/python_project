class Receipt:
    def __init__(self):
        self.items = []
        self.total_price = 0.0

    def add_item(self, product, price, quantity):
        total_price = price * quantity
        self.items.append({'product': product, 'price': price, 'quantity': quantity, 'total_price': total_price})
        self.total_price += total_price