class Solution:
    # time : 3n ~ O(n)
    # space: n due to r[] ~ O(n)
    def trap(self, height: List[int]) -> int:
        n = len(height)

        r = [None] * n
        r[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            r[i] = max(r[i + 1], height[i])

        ans = 0
        maxSoFar = 0  # li
        for i in range(n):
            # find the water trapped on top of the ith building
            maxSoFar = max(maxSoFar, height[i])
            wi = min(maxSoFar, r[i]) - height[i]
            ans += wi

        return ans
