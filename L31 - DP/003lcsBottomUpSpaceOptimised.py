# time : O(mn)
# space: O(n) due to dp[]
def f_bottom_up_space_optimised(s1: str, s2: str, m: int, n: int) -> int:
    dp = [0] * (n + 1)  # at present dp[] stores the mth row
    for i in range(m - 1, -1, -1):
        diag = 0
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                cur_ans = 1 + diag
                diag = dp[j]
                dp[j] = cur_ans
            else:
                diag = dp[j]
                dp[j] = max(dp[j + 1], dp[j])

    # at this point of time, dp[] stores the 0th row
    return dp[0]  # at the 0th index of dp[] we store f(0, 0)


s1 = input()
m = len(s1)

s2 = input()
n = len(s2)

print(f_bottom_up_space_optimised(s1, s2, m, n))
