# 6-3
glossary = {
  'loop': 'a method of iteration',
  'list': 'a collection of data',
  'dictionary': 'a collection for look-up',
  'indentation': 'when you indent something',
  'tuple': 'an immutable list',
}

# Print each word and its meaning
print("A loop is " + glossary['loop'] + ".")
print("A list is " + glossary['list'] + ".")
print("A dictionary is " + glossary['dictionary'] + ".")
print("Indentation is " + glossary['indentation'] + ".")
print("A tuple is " + glossary['tuple'] + ".")

# Use a for loop to print each word and definitiion
for word, definition in glossary.items():
  if word == 'indentation':
    print(word.title() + " is " + definition + ".")
  else:
    print("A " + word + " is " + definition + ".")