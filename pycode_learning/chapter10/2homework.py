# homework 10-1
with open('pycode_learning/chapter10/learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('pycode_learning/chapter10/learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('pycode_learning/chapter10/learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# homework 10-2
with open('pycode_learning/chapter10/learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.replace('Python', 'C').rstrip())