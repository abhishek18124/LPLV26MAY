class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def f(
            n: int,
            board: list[list[str]],
            i: int,
            cols: set[int],
            right_diag: set[int],
            left_diag: set[int],
        ):
            # base case
            if i == n:
                all_boards.append(["".join(row) for row in board])
                return

            # recursive case

            # f(i) : take decisions for queens i to n-1

            # decide for Qi

            for j in range(n):
                if j in cols or (i + j) in right_diag or (i - j) in left_diag:
                    continue

                board[i][j] = "Q"
                cols.add(j)
                right_diag.add(i + j)
                left_diag.add(i - j)
                f(n, board, i + 1, cols, right_diag, left_diag)
                board[i][j] = "."  # backtracking
                cols.remove(j)  # backtracking
                right_diag.remove(i + j)  # backtracking
                left_diag.remove(i - j)  # backtracking

        all_boards = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        right_diag = set()
        left_diag = set()

        f(n, board, 0, cols, right_diag, left_diag)

        return all_boards
