# time : O(n)


def all_occ(arr: list[int], t: int) -> None:
    flag = False  # assume t is not present
    for i, num in enumerate(arr):
        if num == t:
            flag = True
            print(i, end=" ")

    if flag == False:
        print(-1)


n = int(input())
t = int(input())

arr = [int(input()) for _ in range(n)]

all_occ(arr, t)
