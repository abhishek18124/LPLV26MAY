class Solution:
    # time : O(n) assuming dict ops are const
    # space: O(n) due dict()

    def longestConsecutive(self, nums: List[int]) -> int:
        start_map = dict()
        for x in nums:
            if x - 1 in start_map:
                start_map[x] = False
            else:
                start_map[x] = True

            if x + 1 in start_map:
                start_map[x + 1] = False

        max_so_far = 0
        for k, v in start_map.items():
            if v:
                # find the len of seq of consecutives elements that start with k
                cnt = 0
                while k in start_map:
                    cnt += 1
                    k += 1
                max_so_far = max(max_so_far, cnt)

        return max_so_far
