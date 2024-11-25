
def main():

    # Writing user input to a file
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    # Open or create the file in write mode
    with open('writing_files/contacts.txt', 'a') as file:  # 'w' mode overwrites existing content
        # Add newline for better formatting
        # I could skip the file path if I had opened writing_files as my project folder when I opened
        # visual studio code
        file.write(name + ', ' + phone + '\n')


main()
