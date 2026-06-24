# time : O(n^2) worst case
# time : O(n) best case
# bubble sort is stable sorting algorithm
def bubble_sort(arr: list[int], n: int) -> None:
    cnt = 0

    for i in range(1, n):  # [1, n)
        # in the ith pass, put the largest
        # value in the unsorted part of the
        # array to its correct position

        flag = False  # assume no swaps will be done in the ith pass

        for j in range(n - i):  # [0, n-i)
            cnt += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True

        if not flag:  # flag == False
            break

    print(cnt)


n = int(input())
arr = [int(input()) for _ in range(n)]

print(arr)  # [50, 40, 30, 20, 10]
bubble_sort(arr, n)
print(arr)  # [10, 20, 30, 40, 50]
