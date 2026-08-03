# time : O(2^n)
# space: O(n) due to fn call stack

cnt1 = 0
cnt2 = 0


def f(n: int) -> int:
    global cnt1
    cnt1 = cnt1 + 1

    # base case
    if n == 0 or n == 1:
        return n

    # recursive case

    # f(n) : find the nth fib. no.

    return f(n - 1) + f(n - 2)


# time : O(n)
# space: O(n) due to fn call stack + dp[]


def f_topdown(n: int, dp: list[int]) -> int:
    global cnt2
    cnt2 += 1

    # lookup
    if dp[n] != -1:
        # we've solved f(n) previously so we can reuse the result
        return dp[n]

    # base case
    if n == 0 or n == 1:
        dp[n] = n
        return dp[n]

    # recursive case

    # f(n) : find the nth fib. no.

    dp[n] = f_topdown(n - 1, dp) + f_topdown(n - 2, dp)
    return dp[n]


n = int(input())
print(f(n))

dp = [-1] * (n + 1)
print(f_topdown(n, dp))

print(cnt1)
print(cnt2)
