class Solution:
    # time : O(n)
    # space: O(n)
    def isValid(self, s: str) -> bool:
        stk = []

        for ch in s:
            match ch:
                case "(" | "{" | "[":
                    stk.append(ch)
                case ")" if stk and stk[-1] == "(":
                    stk.pop()
                case "}" if stk and stk[-1] == "{":
                    stk.pop()
                case "]" if stk and stk[-1] == "[":
                    stk.pop()
                case _:
                    return False

        return not stk
