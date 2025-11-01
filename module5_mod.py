# module5_mod.py

class NumberProcessor:
    def __init__(self):
        """Initialize an empty list to store numbers"""
        self.numbers = []

    def insert_number(self, num):
        """Insert a number into the list"""
        self.numbers.append(num)

    def search_number(self, x):
        """
        Search for number x in the list.
        Returns:
            index (int): 1-based index if found, -1 otherwise.
        """
        try:
            return self.numbers.index(x) + 1  # 1-based index
        except ValueError:
            return -1
