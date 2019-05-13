# 6-2

favorite_numbers = {
  'larry': 42,
  'gary': 3,
  'barry': 384934348,
  'jerry': 10,
}

print("Larry's favorite number is " + str(favorite_numbers['larry']) + ".")
print("Gary's favorite number is " + str(favorite_numbers['gary']) + ".")
print("Barry's favorite number is " + str(favorite_numbers['barry']) + "?")
print("Jerry's favorite number is " + str(favorite_numbers['jerry']) + "!")

# 6-10

favorite_numbers_lists = {
  'larry': [42, 2, 43, 32, 4],
  'gary': [3, 17, 18, 4, 99],
  'barry': [384934348, 1],
  'jerry': [4, 8, 15, 16, 23, 42],
}

for person, numbers in favorite_numbers_lists.items():
  print("\n" + person.title() + "'s favorite numbers are: ")
  for number in numbers:
    print(str(number))