favorite_languages = {
  'larry': 'python',
  'gary': 'c#',
  'barry': 'ruby',
  'jerry': 'python',
}

print("Gary's favorite language is " + 
  favorite_languages['gary'].title() + ".")

for name, language in favorite_languages.items():
  print(name.title() + "'s favorite language is " + 
    language.title() + ".")

# Loop through all keys in a dictionary
for name in favorite_languages.keys():
  print(name.title())

friends = ['larry', 'gary']
for name in favorite_languages.keys():
  print(name.title())

  if name in friends:
    print(" Hi " + name.title() + 
      ", I see your favorite language is " +
      favorite_languages[name].title() + "!")

if 'harry' not in favorite_languages.keys():
  print("Harry, please take our poll!")

# Looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
  print(name.title() + ", thank you for taking the poll.")

# Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
  print(language.title())

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
  print(language.title())

# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the list and some that are not.
people = ['larry', 'carrie', 'terry', 'barry', 'mary']

# Loop through the list, and if that person has taken the poll, then
# print a message thanking them for doing so. If not, please ask them
# to take the poll.
for person in people:
  if person in favorite_languages:
    print(person.title() + ", thank you for taking the poll.")
  else:
    print(person.title() + ", take the poll already. Sheesh.")