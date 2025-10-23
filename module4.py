# module4.py

def main():
    # Read N
    while True:
        try:
            N = int(input("Please enter a positive integer N: "))
            if N <= 0:
                print("N must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Read N numbers
    numbers = []
    print(f"Please enter {N} numbers one by one:")
    for i in range(N):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Read X
    while True:
        try:
            X = int(input("Please enter the integer X to search for: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Search for X
    if X in numbers:
        index = numbers.index(X) + 1  # Index starts from 1
        print(f"{X} is found at position {index}.")
    else:
        print("-1")


if __name__ == "__main__":
    main()
