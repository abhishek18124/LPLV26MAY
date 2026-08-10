# time : O(nk)
# space: O(n) due to dp[]
def f_bottom_up(n: int, k: int) -> int:
    dp = [None] * (n + 1)
    dp[0] = 1  # at the 0th index of dp[] we store f(0)

    for i in range(1, n + 1):  # [1, n]
        # dp[i] stores f(i)

        cnt = 0

        for j in range(1, k + 1):  # [1, k]
            if i - j >= 0:
                cnt += dp[i - j]

        dp[i] = cnt

    return dp[n]  # at the nth index of dp[] we store f(n)


# time : O(n)
# space: O(n) due to dp[]
# [HW] space can be optimised from O(n) to O(k)


def f_bottom_up_time_optimised(n: int, k: int) -> int:
    dp = [None] * (n + 1)

    dp[0] = 1  # a the 0th index of dp[] we store f(0)
    dp[1] = dp[0]

    for i in range(2, k + 1):  # [2, k]
        dp[i] = 2 * dp[i - 1]

    for i in range(k + 1, n + 1):  # [k+1, n]
        dp[i] = 2 * dp[i - 1] - dp[i - k - 1]

    return dp[n]  # at the nth index of dp[] we store f(n)


n, k = map(int, input().split())
print(f_bottom_up(n, k))
print(f_bottom_up_time_optimised(n, k))
