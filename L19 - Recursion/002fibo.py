def f(n: int) -> int:
    # base case
    if n == 0:
        # f(0) : find the 0th fib. no.
        return 0

    if n == 1:
        # f(1) : find the 1st fib. no.
        return 1

    # if n == 0 or n == 1:
    # 	return n

    # recursive case

    # f(n) : find the nth fib. no.

    # 1. ask your friend to find the n-1th fib. no.

    A = f(n - 1)

    # 2. ask your friend to find the n-2th fib. no.

    B = f(n - 2)

    # 3. use the answers given by your friend to build the final answer

    return A + B


n = int(input())
print(f(n))
