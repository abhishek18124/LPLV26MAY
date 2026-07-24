def f(inp: str, out: list[str], i: int) -> None:
    # base case
    if i == len(inp):
        # print(out)
        print("".join(out))
        return

    # recursive case

    # f(i) : take decisions for inp[i...n-1]

    # decide for inp[i]

    # option 1 : include inp[i] to the out[]
    out.append(inp[i])
    f(inp, out, i + 1)
    out.pop()  # undo # backtracking

    # option 2 : exclude inp[i] from the out[]
    f(inp, out, i + 1)


inp = input()
out = []
f(inp, out, 0)
