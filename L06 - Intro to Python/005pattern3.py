n = int(input())

i = 1
num = 1

while i <= n:
    # for the ith row, print i numbers starting from 1 in the increasing order
    j = 1
    while j <= i:
        print(num, end=" ")
        j = j + 1
        num = num + 1

    i = i + 1
    print()

print()
