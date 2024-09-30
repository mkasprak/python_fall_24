# Wednesday 09/18/2024 3.3A Logical Operations

int1 = int(input("Please enter an integer: "))
int2 = int(input("Please enter another integer: "))

if int1 >= 16 and int2 >= 16:
    print("Both numbers are greater than or equal 16")
else:
    print("Not all numbers are greater than or equal 16")

if int1 <= 56 and int2 <= 56:
    print("Both numbers are less than or equal 56")
else:
    print("Not all numbers are less then or equal 56")

if (int1 % 2) == 0 or (int2 % 2) == 0:
    print("Either number is even")
else:
    print("Neither number is even")

if (int1 % 7 == 0) or (int2 % 7 == 0):
    print("Either number is divisible by 7")
else:
    print("Neither number is divisible by 7")

if not int1 > int2:
    print("Integer one is not greater than integer 2.")
else:
    print("Integer one is greater than integer 2.")

if not int2 >= 250:
    print("Integer two is not greater or equal to 250")
else:
    print("Integer two is greater than or equal to 250.")
