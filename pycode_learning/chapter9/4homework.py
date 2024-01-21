# homework 9-4
class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name + " serves wonderful " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print(self.restaurant_name + " is open. Come on in!")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served
restaurant = restaurant('the mean queen', 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("Number served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))
restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))
restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))

# homework 9-5
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
    
    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
user = User('john', 'doe', 'j_doe', 'jdoe@example.com', 'New York')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print("Login attempts: " + str(user.login_attempts))
user.reset_login_attempts()
print("Login attempts: " + str(user.login_attempts))
