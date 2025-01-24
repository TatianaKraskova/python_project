from unit_test_project.src.Receipt import Receipt
from unit_test_project.src.SpecialOfferType import SpecialOfferType  # Import at the top
from unit_test_project.src import FakeCatalog, ShoppingCart, Product

class Teller:
    def __init__(self, catalog: FakeCatalog):
        self.catalog = catalog
        self.special_offers = {}

    def add_special_offer(self, offer_type, product: Product, discount_amount: float):
        self.special_offers[product.name] = (offer_type, discount_amount)

    def checks_out_articles_from(self, cart: ShoppingCart):
        receipt = Receipt()
        for item_name, item in cart.items.items():
            product = item['product']
            quantity = item['quantity']
            price = product.price * quantity

            # Check if the product has a special offer
            if product.name in self.special_offers:
                offer_type, discount_amount = self.special_offers[product.name]

                # Apply the discount if it's a 10% discount
                if offer_type == SpecialOfferType.TEN_PERCENT_DISCOUNT:
                    price -= price * (discount_amount / 100)  # Apply the 10% discount

            receipt.add_item(product, price, quantity)

        return receipt
