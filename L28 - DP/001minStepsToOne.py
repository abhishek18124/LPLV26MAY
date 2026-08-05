import sys
import math

cnt1 = 0

# time : O(3^n)
# space: O(n) due to fn call stack


def f(n: int) -> int:
    global cnt1
    cnt1 += 1

    # base case
    if n == 1:
        return 0

    # recursive case

    # f(n) : find min. steps required to reduce n to 1

    # decide the next step

    # option 1 : reduce n to n-1

    op1 = f(n - 1)

    # option 2 : reduce n to n/2 if n%2 is zero

    op2 = sys.maxsize  # float('inf') # math.inf
    if n % 2 == 0:
        op2 = f(n // 2)

    # option 3 : reduce n to n/3 if n%3 is zero
    op3 = sys.maxsize  # float('inf') # math.inf
    if n % 3 == 0:
        op3 = f(n // 3)

    return 1 + min(op1, op2, op3)


cnt2 = 0

# time : O(n)
# space: n due to dp[] + n due to fn call stack ~ O(n)


def f_topdown(n: int, dp: list[int]) -> int:
    global cnt2
    cnt2 += 1

    # lookup
    if dp[n] != -1:
        # f(n) is solved previously so we can reuse the result
        return dp[n]

    # base case
    if n == 1:
        dp[n] = 0
        return dp[n]

    # recursive case

    # f(n) : find min. steps required to reduce n to 1

    # decide the next step

    # option 1 : reduce n to n-1

    op1 = f_topdown(n - 1, dp)

    # option 2 : reduce n to n/2 if n%2 is zero

    op2 = sys.maxsize  # float('inf') # math.inf
    if n % 2 == 0:
        op2 = f_topdown(n // 2, dp)

    # option 3 : reduce n to n/3 if n%3 is zero
    op3 = sys.maxsize  # float('inf') # math.inf
    if n % 3 == 0:
        op3 = f_topdown(n // 3, dp)

    dp[n] = 1 + min(op1, op2, op3)
    return dp[n]


n = int(input())
print(f(n))

dp = [-1] * (n + 1)  # 0th index is not used
print(f_topdown(n, dp))

print(cnt1)
print(cnt2)
