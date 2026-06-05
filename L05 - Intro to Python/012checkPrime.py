n = int(input())

i = 2

while i * i <= n:
    if n % i == 0:
        print("not prime")
        break
    i = i + 1

if i * i > n:
    print("prime")
