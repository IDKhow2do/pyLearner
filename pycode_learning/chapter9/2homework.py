# homework 9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " serves wonderful " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open. Come on in!")

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
### 这里注意怎么写，一开始错了
restaurant.describe_restaurant()
restaurant.open_restaurant()

# homework 9-2
restaurant1 = Restaurant('the mean queen', 'pizza')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('the moon', 'noodles')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('the sun', 'rice')
restaurant3.describe_restaurant()

# homework 9-3
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
    
    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
    
    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

eric = User('eric', 'matthes', 'e_matthes', 'eric@example.com', 'United States')
eric.describe_user()
eric.greet_user()

john = User('john', 'doe', 'j_doe', 'john@example.com', 'Canada')
john.describe_user()
john.greet_user()

sarah = User('sarah', 'smith', 's_smith', 'sarah@example.com', 'Australia')
sarah.describe_user()
sarah.greet_user()
