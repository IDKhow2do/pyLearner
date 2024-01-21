players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])
print(players[:4]) # if you omit the first index, Python automatically starts your slice at the beginning of the list
print(players[2:]) # A similar syntax works if you want a slice that includes the end of a list.
print(players[-3:]) # To output the last three players on the roster, you can use the slice

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:" + str(my_foods))
print("\nMy friend's favorite foods are:" + str(friend_foods))

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:" + str(my_foods))
print("\nMy friend's favorite foods are:" + str(friend_foods))

