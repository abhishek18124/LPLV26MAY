class Solution:
    # time : O(n)
    # space: O(1)
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                # skip the ith char
                i += 1
            elif not s[j].isalnum():
                # skip the jth char
                j -= 1
            else:
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    # s is not a palindrome
                    return False

        # s is a palindrome
        return True
