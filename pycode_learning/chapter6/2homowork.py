# homework 6-1
#字典的键应该是字符串，自己这里一开始使用的是变量，导致报错
someone = {'first_name': 'zhang', 
           'last_name': 'san', 
           'age': 18, 
           'city': 'beijing'
    }
print(someone['first_name'])
print(someone['last_name'])
print(someone['age'])
print(someone['city'])

# homework 6-2
favorite_numbers = {
    'alice': 7,
    'bob': 8,
    'cindy': 9,
    'david': 10,
    'eric': 11,
    }
print("Alice's favorite number is " + str(favorite_numbers['alice']))
for name, number in favorite_numbers.items():
    print(name.title() + "'s favorite number is " + str(number))

# homework 6-3
glossary = {
    'print': '打印',
    'for': '循环',
    'if': '条件判断',
    'list': '列表',
    'tuple': '元组',
    }
print("print: " + glossary['print'])
print("for: " + glossary['for'])
print("if: " + glossary['if'])
print("list: " + glossary['list'])
print("tuple: " + glossary['tuple'])

