# time : O(2^(m+n))
# space: O(m+n) due to fn call stack

cnt1 = 0


def f(i: int, j: int) -> int:
    global cnt1
    cnt1 += 1

    # base case
    if i == m or j == n:
        return 0

    # recursive case

    # f(i, j) : find the length of the LCS b/w s1[i...m-1] and s2[j...n-1]

    if s1[i] == s2[j]:
        return 1 + f(i + 1, j + 1)
    else:
        return max(f(i + 1, j), f(i, j + 1))

    # return 1 + f(i + 1, j + 1) if s1[i] == s2[j] else max(f(i + 1, j), f(i, j + 1))


cnt2 = 0

# time : (m+1)(n+1).const ~ O(mn)
# space: (m+n) due to fn call stack + (m+1)(n+1) due to dp[][] ~ O(mn)


def f_topdown(i: int, j: int) -> int:
    global cnt2
    cnt2 += 1

    # lookup
    if dp[i][j] is not None:
        # you've solve f(i, j) previously so reuse the result
        return dp[i][j]

    # base case
    if i == m or j == n:
        dp[i][j] = 0
        return dp[i][j]

    # recursive case

    # f(i, j) : find the length of the LCS b/w s1[i...m-1] and s2[j...n-1]

    if s1[i] == s2[j]:
        dp[i][j] = 1 + f_topdown(i + 1, j + 1)
        return dp[i][j]
    else:
        dp[i][j] = max(f_topdown(i + 1, j), f_topdown(i, j + 1))
        return dp[i][j]


s1 = input()
m = len(s1)

s2 = input()
n = len(s2)

print(f(0, 0))

dp = [[None] * (n + 1) for _ in range(m + 1)]

print(f_topdown(0, 0))

print(cnt1)
print(cnt2)
