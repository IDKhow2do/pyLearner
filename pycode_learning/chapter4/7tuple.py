# tuple is a immutable list
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 # TypeError: 'tuple' object does not support item assignment
#dimensions.append(250) # AttributeError: 'tuple' object has no attribute 'append'
for dimension in dimensions:
    print(dimension)

# 可以给存储元组的变量赋值
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensinos:")
for dimension in dimensions:
    print(dimension)
# 不能给元组中的元素赋值，但是可以给存储元组的变量赋值
# 相比于列表，元组是更简单的数据结构，如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组
