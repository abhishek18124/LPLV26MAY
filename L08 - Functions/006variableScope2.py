a = 3


def f():
    b = 4

    def g():
        c = 5
        return a * b * c

    return g()


print(f())
