n = int(input())

i = 1

while i <= n:
    # for the ith row, print i stars
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1

    i = i + 1
    print()

print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print()

for i in range(1, n + 1):
    for _ in range(i):
        print("*", end=" ")
    print()
