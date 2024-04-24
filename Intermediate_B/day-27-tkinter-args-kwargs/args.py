def add(*args):
    if args:
        print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add())
print(add(3, 3, 5, 10))

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])

calculate(add=1, multiply=2)

def deep_calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)

deep_calculate(2, add=1, multiply=2)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)

def deeper_calculate(n, *args, **kwargs):
    print(n, args, kwargs)

deeper_calculate(4, 5, 6, 7, x=10, y=15)
