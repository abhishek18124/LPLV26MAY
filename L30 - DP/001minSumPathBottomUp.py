# time : O(mn)
# space: O(mn) due to dp[][]
def f_bottomup(grid: list[list[int]], m: int, n: int) -> int:
    dp = [[None] * n for _ in range(m)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp[i][j] = grid[i][j]
            elif i == m - 1:
                dp[i][j] = grid[i][j] + dp[i][j + 1]
            elif j == n - 1:
                dp[i][j] = grid[i][j] + dp[i + 1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])

    # for i in range(m):
    #     print(*dp[i])

    x, y = 0, 0

    while not (x == m - 1 and y == n - 1):
        print(x, y, sep=" ")
        if y + 1 < n and dp[x][y] == grid[x][y] + dp[x][y + 1]:
            y += 1
        else:
            x += 1

    print(x, y, sep=" ")

    return dp[0][0]  # at the 0,0th index of dp[][] we store f(0, 0)


# time : O(mn)
# space: O(n) due to dp[]


def f_bottomup_space_optimised(grid: list[list[int]], m: int, n: int) -> int:
    dp = [None] * n

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp[j] = grid[i][j]
            elif i == m - 1:
                dp[j] = grid[i][j] + dp[j + 1]
            elif j == n - 1:
                dp[j] = grid[i][j] + dp[j]
            else:
                # dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[i+1][j])
                dp[j] = grid[i][j] + min(dp[j + 1], dp[j])

    return dp[0]  # at the 0th index of dp[] we store f(0, 0)


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
print(f_bottomup(grid, m, n))

print(f_bottomup_space_optimised(grid, m, n))
