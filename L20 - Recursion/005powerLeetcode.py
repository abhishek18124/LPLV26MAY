class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(x: float, n: int) -> float:
            # base case
            if n == 0:
                # f(x, 0) : find pow(x, 0)
                return 1

            # recursive case

            # f(x, n) : find pow(x, n)

            # 1. ask your friend to find pow(x, n//2)
            A = f(x, n // 2)

            # 2. use the answer from your friend to build the final answer

            return A * A if n % 2 == 0 else A * A * x

        if n < 0:
            return 1 / f(x, -n)
        else:
            return f(x, n)
