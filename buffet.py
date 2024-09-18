
    """
        Calculate price of buffet, get age of customer
        from customer, under 1 free, 1-12 $1 per year,
        adult 16.95, senior 12.95
    """


#  calculate buffet price based on age
# Get the customer's age
age = int(input("How old is the customer?  "))
# Check if age is less than 1
if age < 1:
    price = 0.00  # Buffet is free for children under 1
# Check if age is between 1 and 12
elif age < 12:
    price = age * 1.00  # Charge $1 for each year of age
# Check if age is 12 or older but less than 65
elif age <= 65:
    price = 16.95  # Standard adult price
# Age is 65 or older
else:
    price = 12.95  # Senior discount price

print(f"The cost will be:  ${price:,.2f}")
