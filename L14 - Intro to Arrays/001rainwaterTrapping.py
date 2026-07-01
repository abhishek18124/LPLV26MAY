class Solution:
    # time : O(n^2) : TLE
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0

        for i in range(n):
            # find the water trapped on top of the ith building

            # li = max(height[0...i])
            li = height[i]
            for j in range(i - 1, -1, -1):
                li = max(li, height[j])

            # ri = max(height[i...n-1])
            ri = height[i]
            for j in range(i + 1, n):
                ri = max(ri, height[j])

            wi = min(li, ri) - height[i]
            ans += wi

        return ans
