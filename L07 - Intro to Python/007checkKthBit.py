n = int(input())
k = int(input())

if (n >> k) & 1:
    print(True)
else:
    print(False)
