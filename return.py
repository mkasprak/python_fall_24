# def add_numbers(number1, number2):
#     # add two numbers together
#     total = number1 + number2
#     return total


# # Using the function
# result = add_numbers(5, 3)
# print("The sum is:", result)


# return the divisor and remainder
def division(num1, num2):
    whole = num1 // num2
    remainder = num1 % num2
    return whole, remainder


w, r = division(12, 7)
print(f"The answer is {w} with a remainder of {r}.")
