prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
# while Ture: 会一直运行下去，直到遇到break
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 7.3.5 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        continue
# continue会跳过下面的代码，直接进入下一次循环，这里不打印偶数
    print(current_number)
    