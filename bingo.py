"""
Program: Sing the song 'Bingo' using code
Summary: This program generates verses of the song "Bingo" with a dog named Bingo. Each verse replaces 
one letter in Bingo's name with a dog emoji until all letters are replaced.
"""


def print_verse(bingo_name):
    """Prints the structure of the song verse with the given dog name."""
    print("There was a farmer who had a dog")
    print(f"And {bingo_name} was his nameo")
    for _ in range(3):
        for letter in bingo_name:
            print(letter.upper(), end=" ")
        print()
    print(f"And {bingo_name} was his nameo")


def main():
    # Initialize the dog's name as a list for character replacement
    dog = list("Bingo")
    replacement_index = len(dog) - 1  # Start replacing from the last letter

    # Loop over each verse of the song
    for _ in range(len(dog) + 1):  # +1 to include the fully replaced name
        bingo = ''.join(dog)  # Join the list to a string for current verse
        print_verse(bingo)  # Print the verse with current name format

        # Replace one letter with emoji for the next verse, if not all replaced
        if replacement_index >= 0:
            dog[replacement_index] = "🐶"
            replacement_index -= 1


# Run the main function to sing the song
main()
