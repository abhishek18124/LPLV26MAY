def isPrime(n: int) -> bool:
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i = i + 1

    return True


def printPrimes(m: int) -> None:
    num = 2
    cnt = 0

    while cnt < m:
        if isPrime(num):
            print(num)
            cnt += 1

        num += 1


m = int(input())
printPrimes(m)
