# 如何传递实参
# 想到了verilog里面复用电路例化的方法，也有着位置传递和关键字传递的区别
# 位置传递
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet(pet_name='harry', animal_type='hamster')
# 需要把pet_name放在形参列表前面，因为会被python当作位置实参
# 使用默认值时,在形参列表中必须先列出没有默认值的形参,再列出有默认值的实参。
# 这让Python依然能够正确地解读位置实参。
def describe_pet(pet_name, animal_type='dog'):  # 默认值
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet(pet_name='willie')

# 等效的函数调用
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet('willie')
describe_pet(pet_name='willie')
# 以上两种调用方式都是可行的

# 一只名为harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
# 以上三种调用方式都是可行的

# 避免实参错误
