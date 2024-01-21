# 想去旅游的地方列表
destinations = ['Kyoto', 'Iceland', 'New Zealand', 'Norway', 'Patagonia']

# 按原始排列顺序打印列表
print("原始列表:")
print(destinations)

# 使用 sorted() 按字母顺序打印这个列表，不修改原列表
print("\n按字母顺序排序后的列表:")
print(sorted(destinations))

# 再次打印列表，确认排列顺序未变
print("\n确认原始列表的排列顺序未变:")
print(destinations)

# 使用 sorted() 按与字母顺序相反的顺序打印这个列表，不修改原列表
print("\n按字母顺序相反排序后的列表:")
print(sorted(destinations, reverse=True))

# 再次打印列表，确认排列顺序未变
print("\n确认原始列表的排列顺序未变:")
print(destinations)

# 使用 reverse() 修改列表元素的排列顺序
destinations.reverse()
print("\n使用 reverse() 修改列表后:")
print(destinations)

# 使用 reverse() 再次修改列表元素的排列顺序
destinations.reverse()
print("\n使用 reverse() 再次修改列表后，恢复原顺序:")
print(destinations)

# 使用 sort() 修改该列表，使其元素按字母顺序排列
destinations.sort()
print("\n使用 sort() 按字母顺序排序列表后:")
print(destinations)

# 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列
destinations.sort(reverse=True)
print("\n使用 sort() 按字母顺序相反排序列表后:")
print(destinations)

# homework 3-9

# homework 3-10