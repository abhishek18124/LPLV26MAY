class Solution:
    # time : 3n ~ O(n)
    # space: 2n due to l[] and r[] ~ O(n)
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l = [None] * n
        l[0] = height[0]
        for i in range(1, n):
            l[i] = max(l[i - 1], height[i])

        r = [None] * n
        r[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            r[i] = max(r[i + 1], height[i])

        ans = 0

        for i in range(n):
            # find the water trapped on top of the ith building
            wi = min(l[i], r[i]) - height[i]
            ans += wi

        return ans
