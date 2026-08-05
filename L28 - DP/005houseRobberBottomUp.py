class Solution:
    # time : O(n)
    # space: O(n) due to dp[]
    # can we optimise space to O(1) ? Yes
    # do we need to maintain dp[] ? Yes
    # [HW] try to optimise space from O(n) to O(1)
    # hint : maintain values of dp[i+1], dp[i+2] in two variables
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None] * (n + 2)

        dp[n] = 0  # at the nth index of dp[] we store f(n)
        dp[n + 1] = 0  # at the n+1th index of dp[] we store f(n+1)

        for i in range(n - 1, -1, -1):  # [n-1, 0]
            # dp[i] = f(i) = find the max. profit from houses[i...n-1]
            # decide for the ith house
            # option 1 : rob the ith house
            op1 = nums[i] + dp[i + 2]
            # option 2 : don't rob the ith house
            op2 = dp[i + 1]
            dp[i] = max(op1, op2)

        return dp[0]
