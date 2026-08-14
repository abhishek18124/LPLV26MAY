class Solution:
    # time : O(mn)

    def isMatch(self, s: str, p: str) -> bool:
        def f(i: int, j: int) -> bool:
            # lookup
            if dp[i][j] is not None:
                return dp[i][j]

            # base case
            if i == m and j == n:  # s and p are empty
                dp[i][j] = True
                return dp[i][j]

            if i != m and j == n:  # s is non-empty and p is empty
                dp[i][j] = False
                return dp[i][j]

            if i == m and j != n:  # s is empty and p is non-empty
                flag = True  # assume p[j...n-1] is all '*'
                for k in range(j, n):
                    if p[k] != "*":
                        flag = False
                        break
                dp[i][j] = flag
                return dp[i][j]

            # recursive case

            # f(i, j) : check if p[j...n-1] matches s[i...m-1]

            if s[i] == p[j] or p[j] == "?":
                dp[i][j] = f(i + 1, j + 1)
            elif p[j] == "*":
                dp[i][j] = f(i, j + 1) or f(i + 1, j)
            else:
                dp[i][j] = False

            return dp[i][j]

        m = len(s)
        n = len(p)

        dp = [[None] * (n + 1) for _ in range(m + 1)]

        return f(0, 0)
