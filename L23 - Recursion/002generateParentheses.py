def f(n: int, out: list[str], i: int, oc: int, cc: int):
    # base case
    if oc == n and cc == n:  # i == 2 * n
        print("".join(out))
        return

    # recursive case

    # f(i, oc, cc) : take decisions for out[i...2n-1] s.t. so far oc '(' and cc ')' are used

    # decide which char b/w '(' and ')' will be stored at the the ith index of out

    # option 1 : use '('
    if oc < n:
        out[i] = "("
        f(n, out, i + 1, oc + 1, cc)
        out[i] = None

    # option 2 : use ')'
    if cc < n:
        out[i] = ")"
        f(n, out, i + 1, oc, cc + 1)
        out[i] = None


n = int(input())
out = [None] * (2 * n)
f(n, out, 0, 0, 0)
