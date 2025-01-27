class Book:
    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        """Check if the phonebook is consistent (e.g., no duplicates)."""
        # Example consistency check: Ensure no duplicates in phonebook.
        return len(self.numbers) == len(set(self.numbers.values()))
