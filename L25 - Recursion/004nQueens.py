def f(n: int, board: list[list[str]], i: int):
    def is_valid(j: int):
        # check if we can place the Qi in the jth column of the ith row of the board

        # 1. check if there is a previously placed queen (Q0 to Qi-1) in the jth column
        k = i - 1
        while k >= 0:
            if board[k][j] == "Q":
                # we've found a previously placed queen in the jth column
                # therefore we cannot place the ith queen in the jth column
                return False
            k -= 1

        # 2. check is there is a previously placed queen (Q0 to Qi-1) in the right diagonal of the jth column

        k = i - 1
        step = 1
        while k >= 0 and j + step < n:
            if board[k][j + step] == "Q":
                # we've found a previously placed queen in the right diag of the jth
                # column therefore we cannot place the ith queen in the jth column
                return False
            k -= 1
            step += 1

        # 3. check is there is a previously placed queen (Q0 to Qi-1) in the left diagonal of the jth column

        k = i - 1
        step = 1
        while k >= 0 and j - step >= 0:
            if board[k][j - step] == "Q":
                # we've found a previously placed queen in the left diag of the jth
                # column therefore we cannot place the ith queen in the jth column
                return False
            k -= 1
            step += 1

        return True

    # base case
    if i == n:
        for row in board:
            print("".join(row))
        print()
        return

    # recursive case

    # f(i) : take decisions for queens i to n-1

    # decide for Qi

    for j in range(n):
        if is_valid(j):
            board[i][j] = "Q"
            f(n, board, i + 1)
            board[i][j] = "."  # backtracking


n = int(input())
board = [["."] * n for _ in range(n)]
f(n, board, 0)
