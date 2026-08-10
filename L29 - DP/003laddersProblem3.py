# time : O(k^n)
# space: O(n) due to fn call stack

cnt1 = 0


def f(n: int, k: int) -> int:
    global cnt1
    cnt1 += 1

    # base case
    if n == 0:
        return 1

    # recursive case

    # decide the next step

    cnt = 0

    for j in range(1, k + 1):  # [1, k]
        if n - j >= 0:
            cnt += f(n - j, k)

    return cnt


cnt2 = 0


# time : O(nk)
# space: n due to fn callstack + n due to dp[] ~ O(n)


def f_top_down(n: int, k: int, dp: list[int]) -> int:
    global cnt2
    cnt2 += 1

    # lookup
    if dp[n] != -1:
        # we've solved f(n) previously so we can reuse the result
        return dp[n]

    # base case
    if n == 0:
        dp[n] = 1
        return dp[n]

    # recursive case

    # decide the next step

    cnt = 0

    for j in range(1, k + 1):  # [1, k]
        if n - j >= 0:
            cnt += f_top_down(n - j, k, dp)

    dp[n] = cnt
    return dp[n]


n, k = map(int, input().split())
print(f(n, k))

dp = [-1] * (n + 1)
print(f_top_down(n, k, dp))

print(cnt1)
print(cnt2)
