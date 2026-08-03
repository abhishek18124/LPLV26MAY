# time : O(n)
# space: O(n) due to dp[]


def f_bottom_up(n: int) -> int:
    dp = [None] * (n + 1)
    dp[0] = 0  # at the 0th index of dp[] we store f(0)
    dp[1] = 1  # at the 1st index of dp[] we store f(1)
    for i in range(2, n + 1):  # [2, n]
        # dp[i] stores f(i) = f(i-1) + f(i-2)
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]  # at the nth index of dp[] we store f(n)

# time : O(n)
# space: O(1)

def f_bottom_up_space_optimised(n: int) -> int:
	if n == 0 or n == 1:
		return n

    a = 0  # 0th fib. no
    b = 1  # 1st fib. no

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


n = int(input())
print(f_bottom_up(n))

print(f_bottom_up_space_optimised(n))
