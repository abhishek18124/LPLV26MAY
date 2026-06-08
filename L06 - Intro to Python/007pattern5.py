n = int(input())

for i in range(1, n + 1):
    # for the ith row print n-i spaces
    for _ in range(n - i):
        print(" ", end=" ")

    # followed by i stars
    for _ in range(i):
        print("*", end=" ")

    print()
