age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10")
# 一种更简洁更容易修改的写法
age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# 使用多个 elif 代码块
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10  # 这里的elif是在前一个elif为False的情况下才会执行的
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# 省略else代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age > 65:
    price = 5
elif age >= 65:
    price = 5 #else代码块可以省略，但是elif代码块不能省略,else包罗万象，可能带来意料之外的逻辑
print("Your admission cost is $" + str(price) + ".")
# 测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")
#如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句
