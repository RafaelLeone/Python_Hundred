def add(*args):
    if args:
        print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add())
print(add(3, 3, 5, 10))
