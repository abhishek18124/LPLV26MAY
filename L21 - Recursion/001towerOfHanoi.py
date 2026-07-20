# to move n disks from s to d using h we've to take pow(2, n) - 1 moves
def f(n: int, s: str, d: str, h: str) -> None:
    # base case
    if n == 0:
        # f(0) : move 0 disks from s to d using h
        return

    # recursive case

    # f(n) : move n disks from s to d using h

    # 1. ask your friend to move n-1 disks from s to h using d
    f(n - 1, s, h, d)

    # 2. move the largest disk from s to d
    print(f"move disk from {s} to {d}")

    # 3. ask your friend to move n-1 disks from h to d using s
    f(n - 1, h, d, s)


n = int(input())
f(n, "A", "C", "B")
