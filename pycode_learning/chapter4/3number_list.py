for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)    

number = list(range(1, 6))
print(number)
even_number = list(range(2, 11, 2))     #设置了步长
print(even_number)

squares = []
for value in range(1, 11):
    squre = value ** 2
    squares.append(squre)
    print(squares)

# 更简洁的一种写法,不用中间变量square
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)


#列表解析, 一行代码实现
squares = [value ** 2 for value in range(1, 11)]
print(squares)
