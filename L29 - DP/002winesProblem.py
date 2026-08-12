# time : O(2^n)
# space: O(n) due to fn call stack
def f(prices: list[int], i: int, j: int, y: int) -> int:
    # base case
    if i == j:
        return y * prices[i]  # y * prices[j]

    # recursive case

    # f(i, j, y) : find the maximum profits for wine bottles i to j starting from yth year

    # decide for the yth year

    # option 1 : sell the ith bottle in the yth year

    op1 = prices[i] * y + f(prices, i + 1, j, y + 1)

    # option 2 : sell the jth bottle in the yth year

    op2 = prices[j] * y + f(prices, i, j - 1, y + 1)

    return max(op1, op2)


prices = list(map(int, input().split()))
n = len(prices)
print(f(prices, 0, n - 1, 1))
