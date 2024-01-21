# homework 8-9
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
magicians = ['david', 'carolina', 'alice']

# homework 8-10
def make_great(magicians):
    # 使用列表推导式添加 "the Great" 到每个魔术师的名字中
    return ["the Great " + magician for magician in magicians]
magicians = make_great(magicians)
make_great(magicians)
show_magicians(magicians)

# homework 8-11
magicians = ['david', 'carolina', 'alice']
magicians_copy = magicians[:]
make_great(magicians_copy)
show_magicians(magicians_copy)
