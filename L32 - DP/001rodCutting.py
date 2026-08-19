# time : O(n^n * n)
# space: O(n) due to fn call stack

cnt1 = 0


def f(n: int, p: list[int]) -> int:
    global cnt1
    cnt1 += 1
    # base case
    if n == 0:
        return 0

    # recursive case

    # f(n) : find the maximum profit we can make from a rod of length n

    # decide the size of the next cut

    max_so_far = 0

    for j in range(1, n + 1):  # [1, n]
        max_so_far = max(max_so_far, p[j - 1] + f(n - j, p))

    return max_so_far


cnt2 = 0

# time : O(n^2)
# space: n due to fn call + n due to dp ~ O(n)


def f_topdown(n: int, p: list[int], dp: list[int]) -> int:
    global cnt2
    cnt2 += 1
    # lookup
    if dp[n] is not None:
        return dp[n]

    # base case
    if n == 0:
        dp[n] = 0
        return dp[n]

    # recursive case

    # f(n) : find the maximum profit we can make from a rod of length n

    # decide the size of the next cut

    max_so_far = 0

    for j in range(1, n + 1):  # [1, n]
        max_so_far = max(max_so_far, p[j - 1] + f_topdown(n - j, p, dp))

    dp[n] = max_so_far
    return dp[n]


# time : O(n^2)
# space: O(n) due to dp[]


def f_bottom_up(n: int, p: list[int]) -> int:
    dp = [None] * (n + 1)
    dp[0] = 0  # at the 0th index of dp[] we store f(0)
    for i in range(1, n + 1):  # [1, n]
        # dp[i] stores f(i) : find the maximum profit we can make from a rod of length i
        max_so_far = 0
        for j in range(1, i + 1):  # [1, i]
            max_so_far = max(max_so_far, p[j - 1] + dp[i - j])
            dp[i] = max_so_far

    return dp[n]  # at the nth index of dp[] we store f(n)


n = int(input())
p = list(map(int, input().split()))

print(f(n, p))

dp = [None] * (n + 1)
print(f_topdown(n, p, dp))

print(cnt1)
print(cnt2)

print(f_bottom_up(n, p))
