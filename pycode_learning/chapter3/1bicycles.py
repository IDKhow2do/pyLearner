bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-3])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# homework 3-1
names = ["李亚男", "马越", "陈书生", "种马" ]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# homework 3-2
for name in names:
    print(f"你好哇，祝你生日快乐{name}！")

# homework 3-3
for i in bicycles:
    print(f"I would like to own a {i}.")
