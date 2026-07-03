class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # time : O(n)
        # space: O(1) but nums[] is modified
        while True:
            x = nums[0]
            if nums[x] == x:
                return x
            nums[0], nums[x] = nums[x], nums[0]
