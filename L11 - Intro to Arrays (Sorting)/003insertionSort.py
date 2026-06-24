# stable sorting algorithm
# time : O(n^2) worst case e.g. 50 40 30 20 10
# time : O(n) best e.g. 10, 20, 30, 40, 50
def insertion_sort(arr: list[int], n: int) -> None:
    for i in range(1, n):  # [1, n)
        key = arr[i]
        # in the ith pass, insert the key to
        # its correct position in the sorted
        # part of the arr
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


n = int(input())
arr = [int(input()) for _ in range(n)]

print(arr)  # [50, 40, 30, 20, 10]
insertion_sort(arr, n)
print(arr)  # [10, 20, 30, 40, 50]
