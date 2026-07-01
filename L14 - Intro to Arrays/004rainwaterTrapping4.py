class Solution:
    # time : O(n)
    # space: O(1)
    def trap(self, height: List[int]) -> int:
        n = len(height)

        i, j = 0, n - 1

        l = 0  # float('-inf') # height[0]
        r = 0  # float('-inf') # height[n-1]

        ans = 0

        while i <= j:
            l = max(l, height[i])
            r = max(r, height[j])

            if l < r:
                wi = l - height[i]
                ans += wi
                i += 1
            else:
                wj = r - height[j]
                ans += wj
                j -= 1

        return ans
