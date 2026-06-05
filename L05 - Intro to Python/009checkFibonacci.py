n = int(input())
if n == 0 or n == 1:
    print(True)
else:
    a = 0  # 0th fib. no.
    b = 1  # 1st fib. no.

    while True:
        c = a + b
        if c == n:
            print(True)
            break
        elif c > n:
            print(False)
            break
        else:
            a = b
            b = c
