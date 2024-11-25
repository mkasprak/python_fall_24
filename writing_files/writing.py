
def main():
    # Writing user input to a file
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    # Open or create the file in write mode
    with open('contacts.txt', 'w') as file:
        file.write(name + ', ' + phone)


main()
