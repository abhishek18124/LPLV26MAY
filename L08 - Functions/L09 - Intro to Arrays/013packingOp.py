def add(*a, b, c):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    return sum(a) + b + c


print(add(2, b=3, c=5))
print(add(2, 3, b=5, c=6))
print(add(2, 3, 5, b=6, c=7))
