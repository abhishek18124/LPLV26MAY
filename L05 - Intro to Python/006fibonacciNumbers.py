n = int(input())
if n == 0 or n == 1:
    print(n)
else:
    # n >= 2
    a = 0  # 0th fib. no.
    b = 1  # 1st fib. no.

    i = 1

    # iterations = n-1 ~ n
    # work done in each iteration ~ const
    # time : n.const ~ O(n)

    while i <= n - 1:
        c = a + b
        a = b
        b = c
        i = i + 1

    print(c)
