bits = []

# time : logn due to f() + logn due to join ~ O(logn)
# space: logn due to bits + logn due to fn call stack ~ O(logn)


def f(n: int) -> None:
    # base case
    if n == 0:
        # f(0) : find the binary string for 0
        bits.append("0")
        return

    # recursive case

    # f(n) : find the binary string for n

    # 1. ask your friend to find the binary string for n//2

    f(n // 2)

    # 2. use the answer from your friend to get the binary string for n

    bits.append(str(n % 2))


n = int(input())
f(n)
print("".join(bits))
