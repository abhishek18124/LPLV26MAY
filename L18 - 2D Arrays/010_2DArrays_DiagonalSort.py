class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort(i: int, j: int) -> None:
            # sort the diagonal that starts at the i,jth index
            diag = []
            diag_len = min(m - i, n - j)
            for k in range(diag_len):
                diag.append(mat[i + k][j + k])

            diag.sort()
            for k in range(diag_len):
                mat[i + k][j + k] = diag[k]

        m, n = len(mat), len(mat[0])
        for i in range(m):
            sort(i, 0)

        for j in range(1, n):
            sort(0, j)

        return mat

        # assume x = min(m, n)
        # time : (m+n-1) * (x + x*logx + x)
        # time : (m+n-1) * (x * logx)
        # space: x due diag[]
