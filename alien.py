# A simple dictionary
alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'}

print(alien_0['color'])
print(alien_0['points'])

# Accessing values in a dictionary
new_points = alien_0['points']

print("You just earned " + str(new_points) + " points!")

# Adding key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Starting with an empty dictionary
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

# Modifying values in a dictionary
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'

print("The alien is now " + alien_0['color'] + ".")

# Giving alien 0 some movement
if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Remove key-value pair
del alien_0['points']
print(alien_0)