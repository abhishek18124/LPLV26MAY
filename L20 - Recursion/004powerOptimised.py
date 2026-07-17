def f(x: int, n: int) -> int:
    # base case
    if n == 0:
        # f(x, 0) : find pow(x, 0)
        return 1

    # recursive case

    # f(x, n) : find pow(x, n)

    # 1. ask your friend to find pow(x, n//2)
    A = f(x, n // 2)

    # 2. use the answer from your friend to build the final answer

    # if n % 2 == 0:
    #     # n is even
    #     return A * A
    # else:
    #     # n is odd
    #     return A * A * x

    return A * A if n % 2 == 0 else A * A * x


x, n = map(int, input().split())
print(f(x, n))
