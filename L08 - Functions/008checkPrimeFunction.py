def isPrime(n: int) -> bool:
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i = i + 1

    return True


num = int(input())
print(isPrime(num))
