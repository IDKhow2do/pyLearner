# Define a tuple of five simple foods
foods = ('pizza', 'burger', 'pasta', 'salad', 'soup')

# Print the five foods using a for loop
for food in foods:
    print(food)

# Attempt to modify an element of the tuple
# This will raise a TypeError
# foods[0] = 'sushi'

# Replace two foods in the tuple
foods = ('sushi', 'steak', 'pasta', 'salad', 'soup')

# Print the new tuple using a for loop
for food in foods:
    print(food)
