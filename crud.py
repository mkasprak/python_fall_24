"""
    _summary_
    CRUD - Create, Read, Update, Delete
"""

def menu():
    try:
        customer = check()
        print(customer)  # error checking can delete
        print("Greetings! What would you like to do today?")
        choice = 0
        while choice != 5:
            print("\n1.  Search for and display a record.")
            print("2.  Create a new record.")
            print("3.  Update an existing record")
            print("4.  Delete an existing record")
            print("5.  Quit the program.")
            try:
                choice = int(input("Please enter the number of your selection: "))
                if choice == 1:
                    display(customer)
                elif choice == 2:
                    create(customer)
                elif choice == 3:
                    update(customer)
                elif choice == 4:
                    delete(customer)
                elif choice == 5:
                    print("Goodbye!")
                else:
                    print("That wasn't one of the options—please try again.")
            except ValueError:
                print("Please enter a number between 1 and 5.")

    except Exception as e:
        print("Invalid!", e)

def check():
    try:
        with open("data.txt", 'r') as file:
            customers = file.readlines()
            return customers
    except FileNotFoundError:
        customers = []
        return customers
    except Exception as e:
        print("Unsuccessful:", e)
        return []

def create(customers):
    print("\nCreate a new record!")
    f_name = input("Please enter the first name: ").capitalize()
    l_name = input("Please enter the last name: ").capitalize()
    email = input("Please enter the email:  ")
    record = f_name + "," + l_name + "," + email + "\n"
    customers.append(record)
    save(customers)

# TODO: Implement optional read() function
# def read(customers):
#     print("Read function - optional for student implementation")


def update(customers):
    try:
        print("\nWe will update an existing record.")
        account = find(customers)
        if isinstance(account, int):
            changeme = customers[account].strip().split(",")
            print(f"Account Found!\nCurrent Record: {customers[account]}")
            print("\nWhat would you like to change?")
            print("1:  Change First Name\n2:  Change Last Name\n3:  Change Email")
            choice = int(input("Please enter the number of the value that you want to change:  "))

            if choice == 1:
                fname = input("Please enter the new first name:  ")
                changeme[0] = fname
            elif choice == 2:
                lname = input("Please enter the new last name:  ")
                changeme[1] = lname
            elif choice == 3:
                email = input("Please enter the new email:  ")
                changeme[2] = email
            else:
                print("That is not a valid choice")

            change = ",".join(changeme) + "\n"
            customers[account] = change
            print("Updated Record:", change)
            save(customers)
        else:
            print(account)

    except Exception as e:
        print("Not a valid menu choice,", e)

def delete(customers):
    print("\nDelete a record")
    index = find(customers)
    if isinstance(index, int):
        print(f"Deleting: {customers[index]}")
        customers.pop(index)
        save(customers)
    else:
        print(index)


def find(customers):
    print("Let me look for that record for you.")
    email = input("Please enter the email you want to look for: ")
    for i, line in enumerate(customers):
        record = line.strip().split(',')
        if len(record) == 3 and record[2] == email:
            print("Found!", line.strip())
            return i
    return "I'm sorry, that record does not exist."


def display(customers):
    print("\nDisplay a record")
    index = find(customers)
    if isinstance(index, int):
        fields = customers[index].strip().split(',')
        print("First Name:", fields[0])
        print("Last Name:", fields[1])
        print("Email:", fields[2])
    else:
        print(index)


def save(customers):
    try:
        with open("data.txt", "w") as file:
            for line in customers:
                file.write(line)
        print("\nSuccessfully saved.")
    except Exception as e:
        print("Oops. That didn't work!", e)

def main():
    menu()

main()
