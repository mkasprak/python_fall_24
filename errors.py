"""_summary_
       Sample using try and except
    """


def main():
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"10 divided by {number} is: {result}")

    except ZeroDivisionError:
        print("Oops! Can't divide by zero. Try a different number.")
        main()
    except ValueError:
        print("Oh no! That isn't a number!")
        main()
    except Exception as e:
        print(f"That isn't valid input!\n {e}")
        main()


main()
