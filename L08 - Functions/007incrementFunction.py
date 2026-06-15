def incr(x: int) -> None:
    x = x + 1
    return x


a = 10
print("before incr()", a)
a = incr(a)
print("after incr()", a)
