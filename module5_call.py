# module5_call.py

from module5_mod import NumberProcessor

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

    # Search and display result
    result = processor.search_number(X)
    print(result)


# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()
