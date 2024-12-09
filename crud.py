"""
    _summary_
    CRUD - Create, Read, Update, Delete


"""


def menu():
    try:
        customer = check()
        print(customer)  # error checking can delete
        print("Greetings! What would like to do do today?")
        choice = 0
        while choice != 5:
            # menu will dispaly options, accept a number, then call the appropriate function
            print("1.  Search for and display a record.")
            print("2.  Create a new record.")
            print("3.  Update an existing record")
            print("4.  Delete an existing record")
            print("5.  Quit the program.")
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
                print("I don't understand!")

    except Exception as e:
        print("Invalid! ", e)


def check():
    try:
        with open("data.txt", 'r') as file:
            customers = file.readlines()
            return customers
    except FileNotFoundError:
        customers = []
        return customers
    except Exception as e:
        print("Unsuccessfull: ", e)


def create(customers):
    # create a new record, call the save function and save to the external file.
    print("Create a new record!")
    f_name = input("Please enter the first name: ").capitalize()
    l_name = input("Please enter the last name: ").capitalize()
    email = input("Please enter the email:  ")
    record = f_name + "," + l_name + "," + email + "\n"
    customers.append(record)
    # print(customers)
    save(customers)


# def read(customers):
#     print("read")
#  optionall approach instead of passing around the list
#  Project Creep


def update(customers):
    try:
        print("We will update an existing record. ")
        account = find(customers)
        changeme = customers[account].split(",")
        for item in changeme:
            print(item)

        if (type(account)) == int:
            print("Account Found!")
            print(f"The record is: {customers[account]}")
        else:
            print(f"Record not found!\n{account}")

        # menu for changing item
        choice = True
        while choice:
            print("1:  Change First Name\n2:  Change Last Name\n3:  Change Email")
            choice = int(
                input("Please enter the number of the value that you want to change:  "))

            if choice == 1:
                fname = input("Please enter the new first name:  ")
                changeme[0] = fname
                choice = False
            elif choice == 2:
                lname = input("Please enter the new last name:  ")
                changeme[1] = lname
                choice = False
            elif choice == 3:
                email = input("please enter the new email:  ")
                changeme[2] = email
                choice = False
            else:
                "That is not a valid choice"
                choice = False

        change = ",".join(changeme)
        print(change, "Is the updated record.")
        customers[account] = change
        save(customers)

    except Exception as e:
        print("Not a valid menu choice, ", e)


def delete(customers):
    print("delete")
    # call find, get index
    # pop index
    # call save passing customer


def find(customers):
    # find a customer, return the index of the customer
    # search by phone number
    # return index
    # TODO Note: in VERSION 2 - allow searching by last name
    print("Let me look for that record for you.")
    email = input("Please enter the email you want to look for.")
    my_index = 0
    for line in customers:
        line = line.strip("\n")
        record = line.split(',')

        if record[2] == email:
            print("Found!", line)
            return my_index
        else:
            my_index += 1
    print("\n\nRecord not found for email: ", email)
    return "I'm sorry, that record does not exist\n\n"


def display(customers):
    print("display")
    # call find
    # get back index
    # print a nicely formatted record


def save(customers):
    # called any time a change is made
    # writes the customers list to the data.txt file
    try:
        with open("data.txt", "w") as file:
            for line in customers:
                file.write(line)
        file.close()
        print(customers)
        print("Successfully saved.")
    except Exception as e:
        print("Oops. That didn't work!", e)


def main():
    # menu for user
    # customer will be the list of customer records

    menu()

    # check()  # does the file exist? create it/ copy to list
    # save()  # save the list to a file
    # create()  # create a new record
    # read()  # read records
    # find()  # find and display a record
    # update()  # change a record
    # delete()  # remove a record
    # display()  # display a record


main()
