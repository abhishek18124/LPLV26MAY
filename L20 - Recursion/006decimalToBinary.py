def f(n: int) -> str:
    # base case
    if n == 0:
        # f(0) : find the binary string for 0
        return "0"

    # recursive case

    # f(n) : find the binary string for n

    # 1. ask your friend to find the binary string for n//2

    binaryStrFromMyFriend = f(n // 2)

    # 2. use the answer from your friend to get the binary string for n

    return binaryStrFromMyFriend + str(n % 2)


n = int(input())
print(f(n))
