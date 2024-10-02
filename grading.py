# Ticket sales assignment

# Create list
seats = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
taken = "0"
# Start selling tickets
while taken != "sold out":
    taken = input("Please input the seat you would like: ")
    if taken in seats:
        seats.remove(taken)
    for item in seats:
        print(item)
    if len(seats) == 0:
        print("We are sold out.")
        taken = "sold out"
