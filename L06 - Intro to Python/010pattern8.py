n = int(input())

for i in range(1, n + 1):
    # for the ith row print n-i+1 characters starting with A in increasing order
    ch = "A"
    for _ in range(n - i + 1):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()
