class Solution:
    # time : n + nlogn ~ O(nlogn)
    # space: O(1) but we are modifying the input list 'sticks'
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)  # time : O(n)

        ans = 0

        while len(sticks) > 1:  # time : O(nlogn)
            first_min = heapq.heappop(sticks)
            second_min = heapq.heappop(sticks)
            new_rope_len = first_min + second_min
            ans += new_rope_len
            heapq.heappush(sticks, new_rope_len)

        return ans
