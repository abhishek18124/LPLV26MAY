def f(
    maze: list[list[str]], path: list[list[str]], m: int, n: int, i: int, j: int
) -> None:
    # base case

    if i == m or j == n or i == -1 or j == -1:
        return

    if maze[i][j] == "X":
        return

    if i == m - 1 and j == n - 1:
        path[i][j] = "1"
        for row in path:
            print(*row)
        print()
        return

    # recursive case

    path[i][j] = "1"
    maze[i][j] = "X"

    f(maze, path, m, n, i, j + 1)  # right
    f(maze, path, m, n, i + 1, j)  # down
    f(maze, path, m, n, i, j - 1)  # left
    f(maze, path, m, n, i - 1, j)  # up

    path[i][j] = "0"
    maze[i][j] = "0"


m, n = map(int, input().split())
maze = [input().split() for _ in range(m)]
path = [[0] * n for _ in range(m)]
f(maze, path, m, n, 0, 0)
