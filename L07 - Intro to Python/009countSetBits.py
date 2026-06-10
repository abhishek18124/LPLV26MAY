n = int(input())
cnt = 0

# while n != 0:
#     zerothBit = n & 1
#     if zerothBit == 1:
#         cnt = cnt + 1
#     n = n >> 1

# iterations = ceil(log2(n+1)) ~ logn
# work done in each iteration = const
# time : O(logn)

# while n != 0:
#     cnt = cnt + (n % 2)
#     n = n // 2

while n != 0:
    cnt = cnt + (n & 1)
    n = n >> 1

print(cnt)
