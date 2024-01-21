# homework 5-1
# 测试1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # 应该为 True

# 测试2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # 应该为 False

# 测试3
number = 10
print("\nIs number > 5? I predict True.")
print(number > 5)  # 应该为 True

# 测试4
print("\nIs number <= 5? I predict False.")
print(number <= 5)  # 应该为 False

# 测试5
my_age = 20
print("\nIs my_age == 20? I predict True.")
print(my_age == 20)  # 应该为 True

# 测试6
print("\nIs my_age != 20? I predict False.")
print(my_age != 20)  # 应该为 False

# 测试7
favorite_food = 'pizza'
print("\nIs favorite_food == 'pizza'? I predict True.")
print(favorite_food == 'pizza')  # 应该为 True

# 测试8
print("\nIs favorite_food == 'pasta'? I predict False.")
print(favorite_food == 'pasta')  # 应该为 False

# 测试9
is_tall = False
print("\nIs is_tall? I predict False.")
print(is_tall)  # 应该为 False

# 测试10
is_tall = True
print("\nIs not is_tall? I predict False.")
print(not is_tall)  # 应该为 False


# homework 5-2
# 检查两个字符串相等和不等
string1 = 'TestString'
string2 = 'teststring'
print("Is string1 == string2? I predict False.")
print(string1 == string2)  # 应该为 False

print("\nIs string1.lower() == string2.lower()? I predict True.")
print(string1.lower() == string2.lower())  # 应该为 True

# 使用函数 lower() 的测试
name = 'Python'
print("\nIs name.lower() == 'python'? I predict True.")
print(name.lower() == 'python')  # 应该为 True

print("\nIs name == 'python'? I predict False.")
print(name == 'python')  # 应该为 False

# 检查两个数字相等、不等、大于、小于、大于等于和小于等于
number1 = 10
number2 = 20
print("\nIs number1 == number2? I predict False.")
print(number1 == number2)  # 应该为 False

print("\nIs number1 != number2? I predict True.")
print(number1 != number2)  # 应该为 True

print("\nIs number1 < number2? I predict True.")
print(number1 < number2)  # 应该为 True

print("\nIs number1 > number2? I predict False.")
print(number1 > number2)  # 应该为 False

print("\nIs number1 <= number2? I predict True.")
print(number1 <= number2)  # 应该为 True

print("\nIs number1 >= number2? I predict False.")
print(number1 >= number2)  # 应该为 False

# 使用关键字 and 和 or 的测试
print("\nIs number1 > 5 and number2 < 25? I predict True.")
print(number1 > 5 and number2 < 25)  # 应该为 True

print("\nIs number1 > 15 or number2 < 15? I predict True.")
print(number1 > 15 or number2 < 15)  # 应该为 True

print("\nIs number1 < 5 and number2 < 25? I predict False.")
print(number1 < 5 and number2 < 25)  # 应该为 False

print("\nIs number1 > 15 or number2 > 25? I predict False.")
print(number1 > 15 or number2 > 25)  # 应该为 False

# 测试特定的值是否包含在列表中
my_list = ['apple', 'banana', 'cherry']
print("\nIs 'banana' in my_list? I predict True.")
print('banana' in my_list)  # 应该为 True

print("\nIs 'durian' in my_list? I predict False.")
print('durian' in my_list)  # 应该为 False

# 测试特定的值是否未包含在列表中
print("\nIs 'mango' not in my_list? I predict True.")
print('mango' not in my_list)  # 应该为 True

print("\nIs 'apple' not in my_list? I predict False.")
print('apple' not in my_list)  # 应该为 False
