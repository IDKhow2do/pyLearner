def make_pizza(*toppings):
    # *toppings 中的星号让 Python 创建一个名为 toppings 的空元组，并将收到的所有值都封装到这个元组中。
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    # 遍历元组中的所有值
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 这样不管顾客想在比萨中添加多少配料，这种函数都能妥善地处理。

# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 注意，Python 依然将这个函数视为有一个形参和一个任意数量实参——Python 先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # 将 user_info 中的所有键值对都加入到字典 profile 中
    for key, value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# 形参 **user_info 中的两个星号让 Python 创建一个名为 user_info 的空字典，并将收到的所有名称—值对都封装到这个字典中。
# 在这个函数中，可以像访问其他字典那样访问 user_info 中的名称—值对。

