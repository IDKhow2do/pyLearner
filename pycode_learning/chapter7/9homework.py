# homework 7-8
sandwich_order = ['pastrami', 'tuna', 'pastrami', 'beef', 'pastrami', 'chicken']
finished_sandwiches = []
for sandwich in sandwich_order:
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
print("\n")
print(finished_sandwiches)

# homework 7-9
sandwich_order = ['pastrami', 'tuna', 'pastrami', 'beef', 'pastrami', 'chicken']
print("Pastrami has been sold out.")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')
print(sandwich_order)

# homework 7-10

responses = {}
polling_active = True   # 标识为真
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response  # 将键值对添加到字典中
    print(responses)
# 看是否还有人要参加调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False  # 标识为假
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to go for a visit " + response + ".")