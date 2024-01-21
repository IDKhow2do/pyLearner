message = input("Tell me something, and I will repeat it back to you: ")
print(message)

last_name = input("Please enter your last name: ")
print("Hello, " + last_name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

first_name = input(prompt)
print("\nHello, " + last_name.title() + first_name.title() + "!")

