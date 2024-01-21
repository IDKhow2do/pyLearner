# homework 6-7
# homework 6-1
#字典的键应该是字符串，自己这里一开始使用的是变量，导致报错
someone = {'first_name': 'zhang', 
           'last_name': 'san', 
           'age': 18, 
           'city': 'beijing'
    }
someone2 = {'first_name': 'li', 
            'last_name': 'si', 
            'age': 20, 
            'city': 'shanghai'
    }
someone3 = {'first_name': 'wang', 
            'last_name': 'wu', 
            'age': 25, 
            'city': 'guangzhou'
    }

people = [someone, someone2, someone3]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()

# homework 6-8

pets = [
    {'name': 'Tom', 'type': 'cat', 'owner': 'Alice'},
    {'name': 'Max', 'type': 'dog', 'owner': 'Bob'},
    {'name': 'Charlie', 'type': 'rabbit', 'owner': 'Cindy'}
]

for pet in pets:
    print(f"Name: {pet['name']}")
    print(f"Type: {pet['type']}")
    print(f"Owner: {pet['owner']}")
    print()

# homework 6-9
favorite_places = {
    'Alice': ['Beijing', 'Shanghai', 'Guangzhou'],
    'Bob': ['New York', 'London', 'Paris'],
    'Cindy': ['Tokyo', 'Osaka', 'Kyoto']
    }
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(place)
    print()

# homework 6-10
favorite_numbers = {
    'Alice': [7, 8, 9],
    'Bob': [8, 9, 10],
    'Cindy': [9, 10, 11],
    'David': [10, 11, 12],
    'Eric': [11, 12, 13]
    }
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(number)
    print()

# homework 6-11
cities = {
    'Beijing': {
        'country': 'China',
        'population': '21.54 million',
        'fact': 'Capital of China'
        },
    'New York': {
        'country': 'America',
        'population': '8.623 million',
        'fact': 'Financial center of the world'
        },
    'London': {
        'country': 'England',
        'population': '8.9 million',
        'fact': 'Capital of England'
        }
    }
for city, info in cities.items():
    print(f"{city}:")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")
    print()

# homework 6-12
    