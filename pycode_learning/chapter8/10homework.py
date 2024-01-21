# homework 8-12
def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_sandwich('pepperoni')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')
make_sandwich('mushrooms', 'green peppers', 'extra cheese', 'pepperoni')

# homework 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # 将 user_info 中的所有键值对都加入到字典 profile 中
    for key, value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# homework 8-14
def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    # 将 car_info 中的所有键值对都加入到字典 car 中
    for key, value in car_info.items():
        car[key] = value
        return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
