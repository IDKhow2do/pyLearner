# 这里真的太像实例化电路了，可能就是因为编程语言的基础是电路，所以才导致了这样的“偶然”吧
# 模块化编程，这里的模块化就是把函数分成了两个模块，一个是定义函数，一个是调用函数
# 但是这里的调用函数并不是直接调用，而是通过import调用
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
