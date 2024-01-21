current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# 如果不给一个message初始值，不能与quit进行比较，那么while将无法运行下去
message = ""
while message != "quit":
    message = input(prompt)
    if message != 'quit':
        print(message)

# 使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message =='quit':
        active = False
    else:
        print(message)