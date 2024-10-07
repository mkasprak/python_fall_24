def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    # Example usage:
    num = int(input("Enter a number between 1 and 25."))
    print(fibonacci(num))  # Output: 5


main()
