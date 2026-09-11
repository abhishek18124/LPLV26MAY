class Solution:
    # time : nlogn to build min_heap + nlogn to solve the prob ~ O(nlogn)
    # space: O(n) due to min_heap
    def connectSticks(self, sticks: List[int]) -> int:
        v = []  # internal repr of min_heap

        for s in sticks:
            heapq.heappush(v, s)

        ans = 0

        while len(v) > 1:
            first_min = heapq.heappop(v)
            second_min = heapq.heappop(v)
            new_rope_len = first_min + second_min
            ans += new_rope_len
            heapq.heappush(v, new_rope_len)

        return ans
