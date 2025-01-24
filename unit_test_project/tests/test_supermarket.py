from unit_test_project.src.Product import Product
from unit_test_project.src.ProductUnit import ProductUnit
from unit_test_project.src.FakeCatalog import FakeCatalog
from unit_test_project.src.ShoppingCart import ShoppingCart
from unit_test_project.src.Teller import Teller
from unit_test_project.src.SpecialOfferType import SpecialOfferType
import pytest


@pytest.fixture
def toothbrush():
    return Product("toothbrush", ProductUnit.EACH, 0.99)


@pytest.fixture
def apples():
    return Product("apples", ProductUnit.KILO, 1.99)


@pytest.fixture
def catalog(toothbrush, apples):
    catalog = FakeCatalog()  # Now correctly using the class
    catalog.add_product(toothbrush, 0.99)
    catalog.add_product(apples, 1.99)
    return catalog


@pytest.fixture
def teller(catalog):
    return Teller(catalog)


@pytest.fixture
def cart():
    return ShoppingCart()

def test_ten_percent_discount(teller, cart, toothbrush, apples):
    # Adding special offer for toothbrush
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    # Adding items to the cart
    cart.add_item_quantity(apples, 2.5)
    cart.add_item_quantity(toothbrush, 1)

    # Checking out articles from the cart
    receipt = teller.checks_out_articles_from(cart)

    # Correct total price calculation: apples + discounted toothbrush
    expected_total = (2.5 * 1.99) + (0.99 * 0.9)

    # Running assertions
    assert expected_total == pytest.approx(receipt.total_price(), 0.01)  # Checking total price
    assert 1 == len(receipt.items)  # Only one unique item in the receipt
    receipt_item = receipt.items[0]
    assert apples == receipt_item['product']
    assert 1.99 == receipt_item['price']
    assert 2.5 * 1.99 == pytest.approx(receipt_item['total_price'], 0.01)
    assert 2.5 == receipt_item['quantity']
