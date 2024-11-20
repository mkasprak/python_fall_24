"""_summary_
"""
# Assignment: Handling List Exceptions
# Objective: Write a Python program that handles exceptions related to list operations.
# Your program will start with a predefined list of the top ten performing artists of all time
# and will include functionality to modify this list based on user input.

# Task 1: Modify Artist List: Write a function to replace an artist in the top_artists list. The function should ask the user for an index and a new artist name. Ensure your function catches and handles ValueError for invalid number conversion and IndexError for out-of-range indices.


def main():  # TODO the assignment started with main function am I suppose to give the function a specific name for this assignment
    try:
        top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                       "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]

# Use input() to get user input for the index and new artist name.
# Convert the index input to an integer using int(). This might raise a ValueError if the input is not a valid integer.

        index = int(
            input("Enter the index of the artist you want to replace (0-9): "))
        new_artist = input("Enter the new artist name: ")
# When replacing an artist in the list, accessing an invalid index will raise an IndexError.
        top_artists[index] = new_artist
        print(f"Artist {index} has been replaced with {new_artist}.")
        print("The list of Top Artists have been updated: ", top_artists)

# Task 2: General Error Handling: Modify your function to catch both ValueError and IndexError using a single except block.
# Provide a general error message like "An input error occurred."
# Remember that you can catch multiple exceptions in a single block by using a tuple for general error handling.

    # i first used multiple except blocks but that caused you to also enter the new artist name even though you used index 10 but it fixed with using the single except block.
    except (ValueError, IndexError) as e:
        # TODO understand why the multiple except block didn't work fully I wonder if
        print("An input error occurred.", e)

# I don't think you want the exception block for this assignment commented out
    # except Exception as e: # I don't think you want the exception block for this assignment
    #     print("An unexpected error occurred:", e)

# TODO get more specific with what is inputed because as of now you can input artist name as ### or just a number.


# call the function
main()
