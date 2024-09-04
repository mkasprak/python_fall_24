# working with and formatting numbers
# Variables

hamburger = 3.99
cheese_burger = 4.99
soda = .99
tax = .02

total = (hamburger * 2) + cheese_burger + (2 * soda)
taxed = total * tax
grand_total = total + taxed

print("\n\nYou ordered: ")
print(f"Two hamburgers at ${hamburger} each.")
print(f"One Cheese burger at ${cheese_burger} each.")
print(f"Two sodas at ${soda} each.")
print(f"For a total of: ${total:.2f}")
print(f"With tax of: ${taxed:.2f}")
print(f"You owe: ${grand_total:.2f}")
