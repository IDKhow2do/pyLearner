# homework 10-3
import os
print("\n" + os.getcwd())
name = input("请输入您的名字：")
with open('pycode_learning/chapter10/guest.txt', 'w') as file:
    file.write(name)

# homework 10-4
while True:
    name = input("请输入您的名字：")
    if name == 'q':
        break
    else:
        with open('pycode_learning/chapter10/guest_book.txt', 'a') as file:
            file.write(name + "\n")
        print("Hello, " + name + "!")
        print("You have signed in the guest book.")

# homework 10-5
while True:
    reason = input("请输入您喜欢编程的原因：")
    if reason == 'q':
        break
    else:
        with open('pycode_learning/chapter10/reason.txt', 'a') as file:
            file.write(reason + "\n")
        print("Thank you for your answer!")

