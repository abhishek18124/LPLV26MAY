class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(n: int, out: list[str], all_outputs: list[str], oc: int, cc: int):
            # base case
            if oc == n and cc == n:
                all_outputs.append("".join(out))
                return

            # recursive case

            # f(oc, cc) : take decisions for out[i...2n-1] s.t. so far oc '(' and cc ')' are used

            # decide which char b/w '(' and ')' will be stored at the the ith index of out

            # option 1 : use '('
            if oc < n:
                out.append("(")
                f(n, out, all_outputs, oc + 1, cc)
                out.pop()

            # option 2 : use ')'
            if cc < oc:
                out.append(")")
                f(n, out, all_outputs, oc, cc + 1)
                out.pop()

        all_outputs = []
        out = []  # stores a single combination
        f(n, out, all_outputs, 0, 0)
        return all_outputs
