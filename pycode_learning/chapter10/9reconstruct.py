import json

def greet_user():
    """问候用户，并指出名字"""
    filename = 'pycode_learning/chapter10/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()


# reconstructed version
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
    
def greet_user():
    """问候用户，指出名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'pycode_learning/chapter10/username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")

greet_user()