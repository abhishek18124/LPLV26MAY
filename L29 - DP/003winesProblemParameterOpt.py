# time : O(2^n)
# space: O(n) due to fn call stack
cnt1 = 0


def f(prices: list[int], i: int, j: int) -> int:
    global cnt1
    cnt1 += 1

    n = len(prices)
    y = n - j + i

    # base case
    if i == j:
        return y * prices[i]  # y * prices[j]

    # recursive case

    # f(i, j, y) : find the maximum profits for wine bottles i to j starting from yth year

    # decide for the yth year

    # option 1 : sell the ith bottle in the yth year

    op1 = prices[i] * y + f(prices, i + 1, j)

    # option 2 : sell the jth bottle in the yth year

    op2 = prices[j] * y + f(prices, i, j - 1)

    return max(op1, op2)


# time : O(n^2)
# space: n^2 due to dp[][] + n due to fn call stack ~ O(n^2)
cnt2 = 0


def f_topdown(prices: list[int], i: int, j: int, dp: list[list[int]]) -> int:
    global cnt2
    cnt2 += 1
    # lookup
    if dp[i][j] is not None:
        return dp[i][j]

    n = len(prices)
    y = n - j + i

    # base case
    if i == j:
        dp[i][j] = y * prices[i]  # y * prices[j]
        return dp[i][j]

    # recursive case

    # f(i, j, y) : find the maximum profits for wine bottles i to j starting from yth year

    # decide for the yth year

    # option 1 : sell the ith bottle in the yth year

    op1 = prices[i] * y + f_topdown(prices, i + 1, j, dp)

    # option 2 : sell the jth bottle in the yth year

    op2 = prices[j] * y + f_topdown(prices, i, j - 1, dp)

    dp[i][j] = max(op1, op2)
    return dp[i][j]


prices = list(map(int, input().split()))
n = len(prices)
print(f(prices, 0, n - 1))

dp = [[None] * n for _ in range(n)]
print(f_topdown(prices, 0, n - 1, dp))

print(cnt1)
print(cnt2)
