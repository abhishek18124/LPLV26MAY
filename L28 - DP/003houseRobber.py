class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(i: int) -> int:
            # base case
            if i == n or i == n + 1:
                return 0

            # recursive case

            # f(i) : find the maximum profit we can make from houses[i...n-1]

            # decide for the ith house

            # option 1 : rob the ith house
            op1 = nums[i] + f(i + 2)

            # option 2 : don't rob the ith house
            op2 = f(i + 1)

            return max(op1, op2)

        n = len(nums)
        return f(0)
