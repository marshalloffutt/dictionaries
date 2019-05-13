# 6-1 & 6-7

larry = {
  'first_name': 'larry',
  'last_name': 'whizbang',
  'age': '54',
  'city': 'nashville',
}

gary = {
  'first_name': 'gary',
  'last_name': 'green',
  'age': '37',
  'city': 'san francisco',
}

barry = {
  'first_name': 'barry',
  'last_name': 'bradford',
  'age': '44',
  'city': 'detroit',
}

people = [larry, gary, barry]


# Print out Larry's info
print(larry['first_name'].title() + " " + 
  larry['last_name'].title() + " is " + larry['age'] + 
  " years old, and lives in " + larry['city'].title() + ".")

# Use a loop to print everyone's stuff
for person in people:
  print(person['first_name'].title() + " " + 
  person['last_name'].title() + " is " + person['age'] + 
  " years old, and lives in " + person['city'].title() + ".")