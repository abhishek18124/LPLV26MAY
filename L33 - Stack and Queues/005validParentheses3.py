class Solution:
    # time : O(n)
    # space: O(n)
    def isValid(self, s: str) -> bool:
        stk = []

        mapping = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch not in mapping:
                stk.append(ch)
            else:
                if stk and stk[-1] == mapping[ch]:
                    stk.pop()
                else:
                    return False

        # if len(stk) == 0:
        #     return True
        # else:
        #     return False

        # return len(stk) == 0

        return not stk
