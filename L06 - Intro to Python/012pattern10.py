n = int(input())
m = n - n // 2

# print the 1st half

for i in range(1, m + 1):
    # for the ith row print i stars
    for _ in range(i):
        print("*", end=" ")
    print()

# print the 2nd half

for i in range(1, m):
    # for the ith row print m-i stars
    for _ in range(m - i):
        print("*", end=" ")
    print()
