class Solution:
    # time : O(n)
    # space: O(n) due to dp[] and fn call stack
    def rob(self, nums: List[int]) -> int:
        def f(i: int) -> int:
            # lookup
            if dp[i] != -1:
                # f(i) is solved previously so reuse result
                return dp[i]

            # base case
            if i == n or i == n + 1:
                dp[i] = 0
                return dp[i]

            # recursive case

            # f(i) : find the maximum profit we can make from houses[i...n-1]

            # decide for the ith house

            # option 1 : rob the ith house
            op1 = nums[i] + f(i + 2)

            # option 2 : don't rob the ith house
            op2 = f(i + 1)

            dp[i] = max(op1, op2)
            return dp[i]

        n = len(nums)
        dp = [-1] * (n + 2)
        return f(0)
