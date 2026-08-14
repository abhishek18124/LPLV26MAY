# time : O(mn)
# space: O(mn) due to dp[][]
def f_bottom_up(s1: str, s2: str, m: int, n: int) -> int:
    dp = [
        [0] * (n + 1) for _ in range(m + 1)
    ]  # 0 init make sures that base case cells are filled with the right value

    for i in range(m - 1, -1, -1):  # [m-1, 0]
        for j in range(n - 1, -1, -1):  # [n-1, 0]
            # dp[i][j] = f(i, j) = find the length of the LCS b/w s1[i...m-1] and s2[j...n-1]
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    # for i in range(m + 1):
    #     print(*dp[i])

    ans = []
    x, y = 0, 0

    while not (x == m or y == n):
        if s1[x] == s2[y]:
            ans.append(s1[x])
            x += 1
            y += 1
        elif dp[x][y] == dp[x][y + 1]:
            y += 1
        else:
            x += 1

    print("".join(ans))

    return dp[0][0]  # at the 0,0th index dp[][] we store f(0,0)


s1 = input()
m = len(s1)

s2 = input()
n = len(s2)

print(f_bottom_up(s1, s2, m, n))
