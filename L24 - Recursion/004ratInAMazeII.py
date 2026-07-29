def f(maze: list[list[str]], m: int, n: int, i: int, j: int) -> int:
    # base case
    if i == m or j == n:
        return 0

    if maze[i][j] == "X":
        return 0

    if i == m - 1 and j == n - 1:
        return 1

    # recursive case

    # f(i, j) : find no. of path from i,jth to m-1,n-1th cell

    # decide the next step

    # option 1 : move right

    # j += 1
    # x = f(maze, m, n, i, j)
    # j -= 1

    x = f(maze, m, n, i, j + 1)

    # option 2 : move down

    # i += 1
    # y = f(maze, m, n, i, j)
    # i -= 1

    y = f(maze, m, n, i + 1, j)

    return x + y


m, n = map(int, input().split())
maze = [input().split() for _ in range(m)]
print(f(maze, m, n, 0, 0))
