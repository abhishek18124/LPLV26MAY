class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def f(mid: int) -> bool:
            nonlocal m
            flower_cnt = 0

            for day in bloomDay:
                if day <= mid:
                    flower_cnt += 1
                    if flower_cnt == k:
                        m = m - 1
                        if m == 0:
                            return True
                        flower_cnt = 0
                else:
                    flower_cnt = 0

            return False

        lo, hi = min(bloomDay), max(bloomDay)
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            # can you make 'm' bouquets of 'k' adjacent flowers in 'mid' days
            if f(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
