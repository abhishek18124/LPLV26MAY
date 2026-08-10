import sys

# time : O(2^(m+n))
# space: O(m+n) due to fn call stack

cnt1 = 0


def f(grid: list[list[int]], m: int, n: int, i: int, j: int) -> int:
    global cnt1
    cnt1 += 1

    # base case

    if i == m - 1 and j == n - 1:
        return grid[i][j]

    # recursive case

    # f(i, j) : find the min sum path from i,jth cell to m-1,n-1th cell

    if i == m - 1:
        return grid[i][j] + f(grid, m, n, i, j + 1)

    if j == n - 1:
        return grid[i][j] + f(grid, m, n, i + 1, j)

    # decide the next step

    # option 1 : move right

    x = f(grid, m, n, i, j + 1)

    # option 2 : move down

    y = f(grid, m, n, i + 1, j)

    return grid[i][j] + min(x, y)


# time : O(mn)
# space: (m+n) due to fn call stack + mn due to dp[][] ~ O(mn)

cnt2 = 0


def f_topdown(
    grid: list[list[int]], m: int, n: int, i: int, j: int, dp: list[list[int]]
) -> int:
    global cnt2
    cnt2 += 1

    # lookup
    if dp[i][j] != None:
        # we've solve f(i, j) previously so we can reuse the result
        return dp[i][j]

    # base case

    if i == m - 1 and j == n - 1:
        return grid[i][j]

    # recursive case

    # f(i, j) : find the min sum path from i,jth cell to m-1,n-1th cell

    if i == m - 1:
        dp[i][j] = grid[i][j] + f_topdown(grid, m, n, i, j + 1, dp)
        return dp[i][j]

    if j == n - 1:
        dp[i][j] = grid[i][j] + f_topdown(grid, m, n, i + 1, j, dp)
        return dp[i][j]

    # decide the next step

    # option 1 : move right

    x = f_topdown(grid, m, n, i, j + 1, dp)

    # option 2 : move down

    y = f_topdown(grid, m, n, i + 1, j, dp)

    dp[i][j] = grid[i][j] + min(x, y)
    return dp[i][j]


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
print(f(grid, m, n, 0, 0))

dp = [[None] * n for _ in range(m)]
print(f_topdown(grid, m, n, 0, 0, dp))

print(cnt1)
print(cnt2)
