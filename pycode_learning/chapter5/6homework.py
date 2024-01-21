# homework 5-8
usernames = ['admin', 'john', 'mary', 'alex', 'sarah']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# homework 5-9
usernames = []
if usernames:
    for username in usernames:
        print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

# homework 5-10
current_users = ['admin', 'john', 'mary', 'alex', 'sarah']
new_users = ['admin', 'john', 'james', 'alex', 'sarah']

# 用户列表中的用户名转为小写
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")

# homework 5-11
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
