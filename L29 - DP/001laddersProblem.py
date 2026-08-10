# time : O(k^n)
# space: O(n) due to fn call stack


def f(n: int, k: int, i: int) -> int:
    # base case
    if i == n:
        return 1

    # recursive case

    # f(i) : find no. of ways to go from i to n

    # decide the size of the next step / jump

    cnt = 0

    for j in range(1, k + 1):  # [1, k]
        if i + j <= n:
            cnt += f(n, k, i + j)

    return cnt


n, k = map(int, input().split())
print(f(n, k, 0))
