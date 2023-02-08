def add_numbers(*args):
    print(args) # comes back as a tuple
    total = 0
    for num in args:
        total = total + num
    return total

total = add_numbers(1,2,3,4,5)
print(total)

def person(**kwargs): #kwargs come back looking like a dictionary
    print(kwargs)
    print(type(kwargs))
    if 'age' in kwargs:
        print(f"You are {kwargs.get('age')}")

person(name="Galina", age=34, gender="female")

def order_tacoBell(name, pickupMethod, **orderItems):
    print(f"Order is for {name}")
    print(f"Pickup method is {pickupMethod}")
    price = 0
    for key, value in orderItems.items():
        price = price + 2.35
    print(f"The total price of your order is {price}")
    return price

totalPrice = order_tacoBell("Galina", "drive-through", softTacos=True, mexicanPizza=True, bajaBlastDrink=True)
print(totalPrice)
