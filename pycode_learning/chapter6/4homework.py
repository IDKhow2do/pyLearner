# homework 6-4
glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
}

for key, value in glossary.items():
    print("\nKey: " + key)
    print("value: " + value)

glossary['function'] = 'A named block of code that performs a specific task.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'Any number with a decimal point.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

print("\nUpdated Glossary:")
for key, value in glossary.items():
    print("\nKey: " + key)
    print("value: " + value)

# homework 6-5
rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'huanghe': 'china',
    'mississippi': 'america',
    'amazon': 'brazil',
    }
for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title() + ".")
print("\nThe following rivers are included in this data set:")
for value in rivers.values():
    print(value.title())

# homework 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
people = ['jen', 'sarah', 'edward', 'phil', 'james', 'lily', 'tom']
for person in people:
    if person in favorite_languages.keys():
        print("Thank you for taking the poll, " + person.title() + "!")
    else:
        print(person.title() + ", please take our poll!")
        