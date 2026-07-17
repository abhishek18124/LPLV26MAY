# time : O(n)
# space: O(n) due to fn call stack
def f(n: int) -> None:
    # base case
    if n == 0:
        # f(0) : print nos. from 0 to 1 in the dec. order
        return

    # recursive case

    # f(n) : print nos. from n to 1 in the dec. order

    # 1. print n
    print(n, end=" ")

    # 2. ask your friend to print nos. from n-1 to 1 in dec order
    f(n - 1)


n = int(input())
f(n)
