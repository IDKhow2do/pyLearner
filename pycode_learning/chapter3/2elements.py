motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = popped_motorcycle
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


# homework 3-4
people = ['爱因斯坦', '谢尔顿', '周杰伦', '毛不易']
for person in people:
    print(f"Welcome to my dinner {person}!")

# homework 3-5
print("\nUnfortunately, 周杰伦 can't make it to the dinner.")

# 替换无法出席的嘉宾
people.remove('周杰伦')
people.append('林俊杰')

# 重新打印邀请信息
for person in people:
    print(f"Welcome to my dinner, {person}!")

# homework 3-6
print("我们找到了一个更大的餐桌, We found a bigger table, so it possible for us to invite more guests.\n")
#首位添加嘉宾
people.insert(0, '牛顿')

# 创建一个中间嘉宾的索引号
middle_index = len(people) // 2
people.insert(middle_index, '特斯拉')

#末尾添加嘉宾
people.append('贝多芬')
for person in people:
    print(f"Welcome to my dinner {person}!")


# homework 3-7

print("不好意思，因为餐桌无法及时送达，我只能邀请两位嘉宾共进晚餐。\n")
while len(people) > 2:
    removed_guest = people.pop()
    print(f"很抱歉，{removed_guest}，我无法邀请你来共进晚餐")
for person in people:
    print(f"{person}，你收到我的邀请，请你准时出席晚宴。")

del people[0]
del people[0]
print(people)

# 3-9
print(f"I've invited {len(people)} to my dinner")