# homework 9-13
from collections import OrderedDict
glossary = OrderedDict()
glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'

for word, definition in glossary.items():
    print("\n\t" + word.title() + ": " + definition)

# homework 9-14
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)
    
# 创建一个6面的骰子
die = Die()
# 掷10次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10):
    result = die.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

die = Die(sides=10)
results = []
for roll_num in range(10):
    result = die.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

die = Die(sides=20)
results = []
for roll_num in range(10):
    result = die.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)

# homework 9-15
# 了解 Python 标准库,一个很不错的资源是网站 Python Module of the Week。 请访问 http://pymotw.com/并查看其中的目录, 在其中找一个你感兴趣的模块进行探索,或阅读模块 collections 和 random 的文档。
