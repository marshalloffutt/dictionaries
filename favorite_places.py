#6-9

# Make a dictionary called favorite_places. Use a name for the key, and a list
# of one to three different places forthe value.
favorite_places = {
    'larry': ['jamaica', 'amsterdam', 'london'],
    'gary': ['new york', 'chicago'],
    'barry': ['miami', 'liverpool', 'california'],
    'terry': ['paris']
}

# Using for loops, print the person and their favorite places.
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())