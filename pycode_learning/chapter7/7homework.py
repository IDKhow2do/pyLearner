# homework 7-4
pizza = "\nPlease enter the pizza toppings you want:"
pizza += "\n(Enter 'quit' when you are finished.)"
toppings = ""
while toppings != "quit":
    toppings = input(pizza)
    if toppings != "quit":
        print("We will add " + toppings + " to your pizza.")
        
# homework 7-5
prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' when you are finished.)"
age = ""
while age != "quit":
    age = input(prompt)
    if age != "quit":
        age = int(age)
        if age < 3:
            print("You are free.")
        elif age < 12:
            print("You need to pay $10.")
        else:
            print("You need to pay $15.")

# homework 7-6

#gpt
# homework 7-4 modified with three different exit conditions
pizza = "\nPlease enter the pizza toppings you want:"
pizza += "\n(Enter 'quit' when you are finished.)"

active = True  # 使用变量 active 来控制循环结束的时机
while active:  # 在 while 循环中使用条件测试来结束循环
    toppings = input(pizza)
    
    if toppings == 'quit':
        active = False  # 设置 active 为 False 以结束循环
        continue  # 跳过循环中剩余的语句，进行下一次循环判断
    
    print(f"We will add {toppings} to your pizza.")

# homework 7-4 modified to use a break statement
pizza = "\nPlease enter the pizza toppings you want:"
pizza += "\n(Enter 'quit' when you are finished.)"

while True:  # 无限循环
    toppings = input(pizza)
    
    if toppings == 'quit':
        break  # 使用 break 语句在用户输入'quit'时退出循环
    
    print(f"We will add {toppings} to your pizza.")

# homework 7-5 modified with three different exit conditions
prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' when you are finished.)"

active = True
while active:
    age = input(prompt)
    
    if age == 'quit':
        break  # 使用 break 语句立即退出循环
    
    age = int(age)
    if age < 3:
        print("You are free.")
    elif age < 12:
        print("You need to pay $10.")
    else:
        print("You need to pay $15.")

# homework 7-7
while True:
    print(1)