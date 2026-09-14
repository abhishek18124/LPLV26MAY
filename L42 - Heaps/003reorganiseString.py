class Solution:
    def reorganizeString(self, s: str) -> str:
        cntr = Counter(s)

        h = []  # internal representation of max_heap

        for ch, freq in cntr.items():
            heapq.heappush(h, (-freq, ch))

        ans = ""

        while h:
            if len(h) == 1:
                freq, ch = heapq.heappop(h)
                freq = -freq
                if freq == 1:
                    ans += ch
                else:
                    # freq > 1
                    ans = ""
            else:
                freq1, ch1 = heapq.heappop(h)
                freq1 = -freq1

                freq2, ch2 = heapq.heappop(h)
                freq2 = -freq2

                ans += ch1
                freq1 -= 1

                ans += ch2
                freq2 -= 1

                if freq1 > 0:
                    heapq.heappush(h, (-freq1, ch1))

                if freq2 > 0:
                    heapq.heappush(h, (-freq2, ch2))

        return ans
