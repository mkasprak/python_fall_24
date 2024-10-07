global TAX = 10


def get_height():
    height = float(input("How many inches tall are you?"))
    return height


def get_weight():
    weight = float(input("What do you weigh (lbs)"))
    return weight


def main():
    height = get_height()
    weight = get_weight()
    print(f"Height: {height}, weight {weight}")


main()
