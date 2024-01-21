
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

requested_topping = ['mushrooms', 'onions', 'pineapple']
#in 判断是否在列表中(and, or)
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
#not in 判断是否不在列表中
if user not in banned_users:
    #未被禁言
    print(f"{user.title()}, you can post a response if you wish.")

