import pytest
from testing_In__python.src.phonebook import Phonebook


@pytest.fixture
def phonebook():
    return Phonebook()


@pytest.mark.parametrize(
    "entry1, entry2, is_consistent",
    [
        (("Bob", "12345"), ("Anna", "01234"), True),
        (("Bob", "12345"), ("Sue", "12345"), False),
        (("Bob", "12345"), ("Sue", "123"), False),
    ]
)
def test_is_consistent(phonebook, entry1, entry2, is_consistent):
    phonebook.add(*entry1)
    phonebook.add(*entry2)
    assert phonebook.is_consistent() == is_consistent
