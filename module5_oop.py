# module5_oop.py

class NumberProcessor:
    def __init__(self):
        self.numbers = []  # Initialize empty list

    def insert_number(self, num):
        """Add a number to the list"""
        self.numbers.append(num)

    def search_number(self, x):
        """Return 1-based index of x if found, else -1"""
        try:
            index = self.numbers.index(x) + 1  # Convert to 1-based index
            return index
        except ValueError:
            return -1


def main():
    # Ask for N
    N = int(input("Enter N (positive integer): "))

    # Create instance of NumberProcessor
    processor = NumberProcessor()

    # Read N numbers
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        processor.insert_number(num)

    # Ask for X
    X = int(input("Enter X (integer to search for): "))

    # Search for X and print result
    result = processor.search_number(X)
    print(result)


# Run main only when executed directly
if __name__ == "__main__":
    main()
