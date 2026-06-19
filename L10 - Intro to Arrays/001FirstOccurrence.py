# time : O(n)


def first_occ(arr: list[int], t: int) -> int:
    for i, num in enumerate(arr):
        if num == t:
            return i

    return -1


n = int(input())
t = int(input())

# arr = []
# for _ in range(n):
# 	num = int(input())
# 	arr.append(num)

arr = [int(input()) for _ in range(n)]

print(first_occ(arr, t))

try:
    print(arr.index(t))
except:
    print(-1)
