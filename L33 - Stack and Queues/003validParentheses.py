class Solution:
    # time : O(n)
    # space: O(n)
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stk.append(ch)
            else:
                if stk and ch == ")" and stk[-1] == "(":
                    stk.pop()
                elif stk and ch == "]" and stk[-1] == "[":
                    stk.pop()
                elif stk and ch == "}" and stk[-1] == "{":
                    stk.pop()
                else:
                    return False

        # if len(stk) == 0:
        #     return True
        # else:
        #     return False

        # return len(stk) == 0

        return not stk
