class Solution:
    # time : O(n)
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_so_far = 0

        i, j = 0, n - 1
        while i < j:
            w = j - i
            h = min(height[i], height[j])
            a = w * h
            max_so_far = max(max_so_far, a)
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1

        return max_so_far
