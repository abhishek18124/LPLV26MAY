class Solution:
    # time : O(n^2) -> TLE
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_so_far = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                w = j - i
                h = min(height[i], height[j])
                a = w * h
                max_so_far = max(max_so_far, a)

        return max_so_far
