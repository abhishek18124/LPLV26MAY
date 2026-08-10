import sys


def f(grid: list[list[int]], m: int, n: int, i: int, j: int) -> int:
    # base case
    if i == m or j == n:
        return sys.maxsize  # math.inf

    if i == m - 1 and j == n - 1:
        return grid[i][j]

    # recursive case

    # f(i, j) : find the min sum path from i,jth cell to m-1,n-1th cell

    # decide the next step

    # option 1 : move right

    x = f(grid, m, n, i, j + 1)

    # option 2 : move down

    y = f(grid, m, n, i + 1, j)

    return grid[i][j] + min(x, y)


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
print(f(grid, m, n, 0, 0))
