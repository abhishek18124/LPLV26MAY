class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def f(i: int, j: int) -> bool:
            # base case
            if i == m and j == n:  # s and p are empty
                return True

            if i != m and j == n:  # s is non-empty and p is empty
                return False

            if i == m and j != n:  # s is empty and p is non-empty
                flag = True  # assume p[j...n-1] is all '*'
                for k in range(j, n):
                    if p[k] != "*":
                        flag = False
                        break
                return flag

            # recursive case

            # f(i, j) : check if p[j...n-1] matches s[i...m-1]

            if s[i] == p[j] or p[j] == "?":
                return f(i + 1, j + 1)
            elif p[j] == "*":
                return f(i, j + 1) or f(i + 1, j)
            else:
                return False

        m = len(s)
        n = len(p)

        return f(0, 0)
