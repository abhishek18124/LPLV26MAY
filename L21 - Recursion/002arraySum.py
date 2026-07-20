def f(x: list[int], i: int) -> int:
    # base case
    if i == len(x):
        # f(n) : find the sum of x[n...n-1] = sum([])
        return 0

    # recursive case

    # f(i) : find the sum of x[i...n-1]

    # 1. ask your friend to find the sum of x[i+1...n-1]
    A = f(x, i + 1)

    # 2. use the answer from your friend to build the final answer
    return x[i] + A


x = [10, 20, 30, 40, 50]
print(f(x, 0))
