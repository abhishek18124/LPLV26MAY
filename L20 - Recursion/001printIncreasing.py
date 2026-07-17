# time : O(n)
# space: O(n) due to fn call stack
def f(n: int) -> None:
    # base case
    if n == 0:
        # f(0) : print nos. from 1 to 0 in the inc. order
        return

    # recursive case

    # f(n) : print nos. from 1 to n in the inc. order

    # 1. ask your friend to print nos. from 1 to n-1 in inc order
    f(n - 1)

    # 2. print n
    print(n, end=" ")


n = int(input())
f(n)
