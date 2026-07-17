# time : O(...)
# space: O(...)
def f(x: int, n: int) -> int:
    # base case
    if n == 0:
        # f(x, 0) : find pow(x, 0)
        return 1

    # recursive case

    # f(x, n) : find pow(x, n)

    # 1. ask your friend to find pow(x, n-1)
    A = f(x, n - 1)

    # 2. use the answer given by your friend to build the final answer
    return x * A


x, n = map(int, input().split())
print(f(x, n))
