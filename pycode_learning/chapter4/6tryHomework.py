# homework 4-10
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the first three items in the list
print("The first three items in the list are:")
print(my_list[:3])

# Print three items from the middle of the list
print("Three items from the middle of the list are:")
middle_index = len(my_list) // 2
print(my_list[middle_index-1:middle_index+2])

# Print the last three items in the list
print("The last three items in the list are:")
print(my_list[-3:])

# homework 4-11
pizzas = ['pepperoni', 'mushrooms', 'extra cheese']
friend_pizzas = pizzas[:]
pizzas.append('chicken')
friend_pizzas.append('beef')
print("My favorite pizzas are:")
print(pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

# homework 4-12
