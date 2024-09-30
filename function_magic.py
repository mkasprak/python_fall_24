# def months(years):
#     # calculate how many months old you are (rounded to years)
#     months = 12 * years
#     print(f"You are {months} months old!")


# years = int(input("How many years old are you? "))
# months(years)

def add_numbers(number1, number2):
    # number1 and number2 are parameters
    return number1 + number2


# pass in order
total = add_numbers(5, 7)
print(total)

# override default  order
total = add_numbers(number2=12, number1=7)
print(total)
