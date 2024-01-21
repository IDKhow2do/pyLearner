# homework 10-6
try:
    num1 = input("Enter the first number: ")
    num1 = int(num1)
    num2 = input("Enter the second number: ")
    num2 = int(num2)

except TypeError:
    print("Error: Please enter numeric values.")
except ValueError:
    print("Error: Please enter numeric values.")

else:
    sum = num1 + num2
    print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum) + ".")

# homework 10-7
while True:
    try:
        num1 = input("Enter the first number: ")
        num1 = int(num1)
        num2 = input("Enter the second number: ")
        num2 = int(num2)
    except TypeError:
        print("Error: Please enter numeric values.")
    except ValueError:
        print("Error: Please enter numeric values.")
    else:
        sum = num1 + num2
        print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum) + ".")
        break

# homework 10-8
try:
    with open('pycode_learning/chapter10/cats.txt') as cats:
        for cat in cats:
            print(cat.rstrip())
    with open('pycode_learning/chapter10/dogs.txt') as dogs:
        for dog in dogs:
            print(dog.rstrip())
except FileNotFoundError:
    print("Sorry, the file does not exist.")

# homework 10-9
try:
    with open('pycode_learning/chapter10/cats.txt') as cats:
        for cat in cats:
            print(cat.rstrip())
    with open('pycode_learning/chapter10/dogs.txt') as dogs:
        for dog in dogs:
            print(dog.rstrip())
except FileNotFoundError:
    pass

# homework 10-10

