import pytest
from testing_In__python.src.phonebook import Phonebook


@pytest.fixture
def phonebook():
    return Phonebook()


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "12345")
    number = phonebook.lookup("Bob")
    assert number == "12345"


def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")


def test_empty_phonebook_is_consistent(phonebook):
    is_consistent = phonebook.is_consistent()
    assert is_consistent


def test_is_consistent_with_different_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Anna", "012345")
    assert phonebook.is_consistent()


def test_is_consistent_with_duplicate_entries(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "12345")
    assert not phonebook.is_consistent()


def test_is_consistent_with_different_prefix(phonebook):
    phonebook.add("Bob", "12345")
    phonebook.add("Sue", "123")
    assert not phonebook.is_consistent()
