import sys

# time : O(n)
# space: O(n) due to dp[]


def f_bottom_up(n: int) -> int:
    dp = [None] * (n + 1)
    dp[1] = 0  # at the 0th idx of dp[] we store f(1)
    for i in range(2, n + 1):  # [2, n]
        # dp[i] = f(i) = min. steps required to reduce i to 1
        # decide the next step
        # option 1 : reduce i to i - 1
        op1 = dp[i - 1]
        # option 2 : reduce i to i // 2 if i%2 is zero
        op2 = sys.maxsize
        if i % 2 == 0:
            op2 = dp[i // 2]
        # option 3 : reduce i to i // 3 if i%3 is zero
        op3 = sys.maxsize
        if i % 3 == 0:
            op3 = dp[i // 3]
        dp[i] = 1 + min(op1, op2, op3)
    return dp[n]  # at the nth idx of dp[] we store f(n)


n = int(input())
print(f_bottom_up(n))
