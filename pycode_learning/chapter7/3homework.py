# homework 7-1
car = input("What kind of car do you want to rent? ")
print("Let me see if I can find you a " + car + ".")

# homework 7-2
people = input("How many people are there? ")
people = int(people)
if people > 8:
    print("There is no empty table.")
else:
    print("There is an empty table.")

# homework 7-3
number = input("Please enter a number: ")
number = int(number)
if number % 10 == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is not a multiple of 10.")
