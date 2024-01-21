# class
class Dog():
    """一次模拟小狗的简单尝试"""
# 这里初始化的是Dog一定包含的name, age, 剩下的在后面定义
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 访问属性
print(my_dog.name)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + ' years old.')
your_dog.sit()
your_dog.roll_over()
