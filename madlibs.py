def song(name, adjective, animal, place, noun1, noun2):
    print("\n\n")
    print(f"{name} had a {adjective} {animal},")
    print(f"{name} had a {adjective} {animal},")
    print(f"And everywhere that {name} went")
    print(f"The {animal} was sure to go.")
    print()
    print(f"It followed her to {place}")
    print(f"Which was against the {noun1},")
    print(f"It made the {noun2} laugh and play")
    print(f"To see a {animal} at {place}.")


input_name = input("Enter a name: ")
input_adjective = input("Enter an adjective: ")
input_animal = input("Enter an animal: ")
input_place = input("Enter a place: ")
input_noun1 = input("Enter a noun: ")
input_noun2 = input("Enter another noun: ")

song(name=input_name, adjective=input_adjective, animal=input_animal,
     place=input_place, noun1=input_noun1, noun2=input_noun2)
