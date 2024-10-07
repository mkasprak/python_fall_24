# recursion demo

def recursion(x):
    if x > 0:
        print(x)
        x -= 1
        recursion(x)


recursion(10)
