cnt = 0


def f(maze: list[list[str]], m: int, n: int, i: int, j: int) -> bool:
    # base case
    if i == m or j == n:
        return False

    if maze[i][j] == "X":
        return False

    if i == m - 1 and j == n - 1:
        global cnt
        cnt += 1
        return True

    # recursive case

    # f(i, j) : check if there is a path from the i,jth cell to the m-1,n-1th cell

    # decide the next step

    # option 1 : move right

    x = f(maze, m, n, i, j + 1)

    # option 2 : move down

    y = f(maze, m, n, i + 1, j)

    return x or y


m, n = map(int, input().split())
maze = [input().split() for _ in range(m)]
print(f(maze, m, n, 0, 0))
print(cnt)
