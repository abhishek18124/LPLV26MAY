def f(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    return a + b + c


# print(f(2, 3, 5)) # fn call using positional arguments

print(f(b=3, c=5, a=2))  # fn call using keyword arguments
