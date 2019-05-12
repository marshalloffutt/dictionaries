# 6-5
rivers = {
  'nile': 'egypt',
  'mississippi': 'united states',
  'rio grande': 'mexico'
}

# Use a loop to print a sentence about each river
for river, country in rivers.items():
  print("The " + river.title() + " runs through " + 
    country.title() + ".")

# Use a loop to print the name of each river in the dictionary
print("\nThe following rivers are listed in the dictionary:")
for river in rivers.keys():
  print(river.title())

# Use a loop to print the name of each country in the dictionary
print("\nThe following countries are listed in the dictionary:")
for country in rivers.values():
  print(country.title())