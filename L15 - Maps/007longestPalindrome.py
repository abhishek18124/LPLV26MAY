class Solution:
    # time : O(n)
    # space: 52 if we put a-z and A-Z into set
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0

        for ch in s:
            if ch in seen:
                ans += 2
                seen.remove(ch)
            else:
                seen.add(ch)

        if len(seen) > 0:
            ans += 1

        return ans
