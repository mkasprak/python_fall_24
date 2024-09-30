# Global variable
number = 10


def multiply(number):
    # The parameter 'number' shadows the global variable 'number'
    return number * 2


# Calling the function
result = multiply(5)

print("Result:", result)
print("Global number:", number)
