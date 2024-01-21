# homework 10-11 and 10-12
import json

def store_and_retrieve_favorite_number():
    try:
        with open("favorite_number.json") as file:
            favorite_number = json.load(file)
        print("I know your favorite number! It's", favorite_number)
    except FileNotFoundError:
        favorite_number = input("Please enter your favorite number: ")
        with open("favorite_number.json", "w") as file:
            json.dump(favorite_number, file)
        print("Your favorite number has been stored.")

store_and_retrieve_favorite_number()

### homework 10-13

def get_stored_username():
    """如果存储了用户名，就获取"""
    filename = 'pycode_learning/chapter10/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None # 返回None，让函数greet_user()知道该如何处理
    else:
        return username
    
def get_new_username():
    username = input("What is your name? ")
    filename = 'pycode_learning/chapter10/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """欢迎用户"""
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (y/n) ")
        if correct == "y":
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()