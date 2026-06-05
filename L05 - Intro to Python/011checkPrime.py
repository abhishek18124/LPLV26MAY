n = int(input())

i = 2

flag = True  # assume n is prime

while i * i <= n:
    if n % i == 0:
        print("not prime")
        flag = False
        break
    i = i + 1

if flag:
    print("prime")
