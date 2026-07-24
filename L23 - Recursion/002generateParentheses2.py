def f(n: int, out: list[str], oc: int, cc: int):
    # base case
    if oc == n and cc == n:
        print("".join(out))
        return

    # recursive case

    # f(oc, cc) : take decisions for out[i...2n-1] s.t. so far oc '(' and cc ')' are used

    # decide which char b/w '(' and ')' will be stored at the the ith index of out

    # option 1 : use '('
    if oc < n:
        out.append("(")
        f(n, out, oc + 1, cc)
        out.pop()

    # option 2 : use ')'
    if cc < n:
        out.append(")")
        f(n, out, oc, cc + 1)
        out.pop()


n = int(input())
out = []
f(n, out, 0, 0)
