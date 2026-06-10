n = int(input())

print(n.bit_count())

cnt = 0

# iteration = no. of set bits in n
# work done in each iteration = const
# time : O(no. of set bits in n)

while n != 0:
    # turn of the rightmost set bit of n
    n = n & (n - 1)
    cnt = cnt + 1

print(cnt)
