"""

https://cses.fi/ckvo8q5wh/task/1192

input
5 8
########
#..#...#
####.#.#
#..#...#
########

output
3

"""


def dfs(i, j) -> None:  # (i, j) = current node
    # 1. mark the currnet node as visited
    vis[i][j] = True

    # 2. process the current node
    ...

    # 3. explore the neighbors of the current node

    ii = i
    jj = j + 1

    if (
        ii >= 0
        and ii < n
        and jj >= 0
        and jj < m
        and grid[ii][jj] == "."
        and not vis[ii][jj]
    ):
        dfs(ii, jj)

    ii = i
    jj = j - 1

    if (
        ii >= 0
        and ii < n
        and jj >= 0
        and jj < m
        and grid[ii][jj] == "."
        and not vis[ii][jj]
    ):
        dfs(ii, jj)

    ii = i + 1
    jj = j

    if (
        ii >= 0
        and ii < n
        and jj >= 0
        and jj < m
        and grid[ii][jj] == "."
        and not vis[ii][jj]
    ):
        dfs(ii, jj)

    ii = i - 1
    jj = j

    if (
        ii >= 0
        and ii < n
        and jj >= 0
        and jj < m
        and grid[ii][jj] == "."
        and not vis[ii][jj]
    ):
        dfs(ii, jj)


n, m = map(int, input().split())
grid = [input() for _ in range(n)]
vis = [[False] * m for _ in range(n)]

cnt = 0  # stores no. of rooms in the building

for i in range(n):
    for j in range(m):
        if grid[i][j] == "." and not vis[i][j]:
            cnt += 1
            dfs(i, j)

print(cnt)
