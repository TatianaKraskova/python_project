import pytest
from unit_testing_with_Python3.src.book import Book

@pytest.fixture
def book():
    """Fixture to initialize a new Book instance for each test."""
    return Book()

def test_lookup_by_name(book):
    book.add('Bob', '12345')
    number = book.lookup('Bob')
    assert number == '12345'

def test_missing_name(book):
    with pytest.raises(KeyError):
        book.lookup('missing')

def test_empty_phonebook_is_consistent(book):
    assert book.is_consistent()

# import unittest
#
# from unit_testing_with_Python3.src.book import Book
#
#
# class BookTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.book = Book()
#
#     #def tearDown(self)-> None:
#     #    pass
#
#     def test_lookup_by_name(self):
#         self.book.add('Bob', '12345')
#         number = self.book.lookup('Bob')
#         self.assertEqual('12345', number)
#
#     def test_missing_name(self):
#         with self.assertRaises(KeyError):
#             self.book.lookup('missing')
#
#    # @unittest.skip('WIP - work in progress')
#     def test_empty_phonebook_is_consistent(self):
#         self.assertTrue(self.book.is_consistent())
