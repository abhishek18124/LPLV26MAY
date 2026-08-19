class Solution:
    # time : O(nk)
    # space: n due to dp[] ~ O(n)
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        dp = [None] * (n + 1)
        dp[n] = 0  # at the nth index of dp[] we store f(n)

        for i in range(n - 1, -1, -1):
            # f(i) : find the maximum sum from partitioning arr[i...n-1]

            # decide the next cut
            max_so_far = 0
            max_ij = 0

            for j in range(i, i + k):  # [i, i+k-1]
                if j < n:
                    max_ij = max(max_ij, arr[j])
                    max_so_far = max(max_so_far, (j - i + 1) * max_ij + dp[j + 1])
                else:
                    break

            dp[i] = max_so_far

        return dp[0]  # at the 0th index of dp[] we store f(0)
