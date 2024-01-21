# homework 8-3
def make_shirt(size, words):
    print("The size of the shirt is " + size + ".")
    print("The words on the shirt is " + words + ".")

make_shirt('M', 'I love python')

# homework 8-4
def make_shirt(size, words='I love python'):
    print("The size of the shirt is " + size + ".")
    print("The words on the shirt is " + words + ".")

make_shirt('M')
make_shirt('S')
make_shirt('L', 'I love Verilog')

# homework 8-5
def describe_city(city, country='China'):
    print(city + " is in " + country + ".")
describe_city('Shanghai')
describe_city('Beijing')
describe_city('Tokyo', 'Japan')
