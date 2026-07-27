def f(inp: str, out: list[str], used: list[bool], i: int) -> None:
    # base case
    if i == len(inp):
        print("".join(out))
        return

    # recursive case

    # f(i) : take decisions for out[i...n-1]

    # decide for ith slot of the out[]

    for j in range(len(inp)):
        if used[j] == False:
            out.append(inp[j])
            used[j] = True
            f(inp, out, used, i + 1)
            out.pop()  # backtracking
            used[j] = False  # backtracking


inp = input()
n = len(inp)

used = [False] * n
out = []

f(inp, out, used, 0)
