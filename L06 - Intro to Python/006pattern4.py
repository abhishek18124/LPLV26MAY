n = int(input())

i = 1

while i <= n:
    # if i % 2 == 0:
    #     num = 0
    # else:
    #     num = 1

    num = 0 if i % 2 == 0 else 1

    j = 1

    while j <= i:
        print(num, end=" ")
        num = 1 - num
        j = j + 1

    i = i + 1
    print()
