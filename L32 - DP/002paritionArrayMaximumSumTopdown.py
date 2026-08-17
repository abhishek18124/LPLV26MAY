class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        def f(i: int) -> int:
            # lookup
            if dp[i] is not None:
                return dp[i]

            # base case
            if i == n:
                dp[i] = 0
                return dp[i]

            # recursive case

            # f(i) : find the maximum sum from partitioning arr[i...n-1]

            # decide the next cut

            max_so_far = 0
            max_ij = 0

            for j in range(i, i + k):  # [i, i+k-1]
                if j < n:
                    max_ij = max(max_ij, arr[j])
                    max_so_far = max(max_so_far, (j - i + 1) * max_ij + f(j + 1))
                else:
                    break

            return dp[i]=max_so_far

        dp = [None] * (n+1)
        return f(0)
