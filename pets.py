# 6-8 Pets:

# Make several dictionaries, where the name of each dictionary is the name of a pet
bill = {
    'name': 'bill',
    'animal_type': 'dog',
    'owner': 'larry',
}

fred = {
    'name': 'fred',
    'animal_type': 'cat',
    'owner': 'gary',
}

george = {
    'name': 'george',
    'animal_type': 'fish',
    'owner': 'barry',
}

jason = {
    'name': 'jason',
    'animal_type': 'dog',
    'owner': 'jerry',
}

jeffrey = {
    'name': 'jeffrey',
    'animal_type': 'cat',
    'owner': 'terry',
}

titus = {
    'name': 'titus',
    'animal_type': 'dog',
    'owner': 'berry',
}

michael = {
    'name': 'michael',
    'animal_type': 'cat',
    'owner': 'larry',
}

# Store the dictionaries in a list called pets
pets = [bill, fred, george, jason, jeffrey, titus, michael]

#Loop through list, print everything about each pet
for pet in pets:
    print("\nHere is all the information for " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))