class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # time : O(n)
        def f(mid: int) -> bool:
            bouquet_cnt = 0
            flower_cnt = 0

            for day in bloomDay:
                if day <= mid:
                    flower_cnt += 1
                    if flower_cnt == k:
                        bouquet_cnt += 1
                        flower_cnt = 0
                else:
                    flower_cnt = 0

            return bouquet_cnt >= m

        lo, hi = min(bloomDay), max(bloomDay)
        ans = -1

        # time : log(hi-lo) * n for doing binary search on answer

        while lo <= hi:  # log(hi-lo) # log(10^9 - 1) # log(10^9) ~ 30 times
            mid = (lo + hi) // 2
            # can you make 'm' bouquets of 'k' adjacent flowers in 'mid' days
            if f(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
