# time : O(n^2)
# space: O(n^2) due to dp[][]
# [HW] space can be optimised from O(n^2) to O(n)
def f_bottom_up(prices: list[int]) -> int:
    n = len(prices)

    dp = [[None] * n for _ in range(n)]

    # fill base case cells
    for i in range(n):
        dp[i][i] = n * prices[i]
        # j = i
        # y = n
        # dp[i][j] = y * prices[i]

    # fill recursive case cells
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            y = n - j + i
            # dp[i][j] = f(i, j) = find the max. profit from wine bottles i to j starting from the yth year
            # decide for the yth year

            # option 1 : sell the ith bottle
            op1 = y * prices[i] + dp[i + 1][j]

            # option 2 : sell the jth bottle

            op2 = y * prices[j] + dp[i][j - 1]

            dp[i][j] = max(op1, op2)

    return dp[0][n - 1]  # at the 0,n-1th index of dp[][] we store f(0, n-1)


prices = list(map(int, input().split()))
print(f_bottom_up(prices))
