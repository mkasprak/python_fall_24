"""_summary_
    exploring and using python modules
    code created by chat gpt
    https://chatgpt.com/share/e/6716a770-d5a8-800e-8282-4cac379ab397
"""

# Import the math module
import math as m  # m is the alias for math

# Objective: Introduce using modules and the pow() function to calculate power

# Get two numbers from the user
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# Use math.pow() to calculate the result
result = m.pow(base, exponent)  # using the alias

# Print the result
print(f"{base} raised to the power of {exponent} is {result}")
