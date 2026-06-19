# time : n/2.const ~ O(n)


def reverse(arr: list[int], n: int) -> None:
    i, j = 0, n - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


n = int(input())
arr = [int(input()) for _ in range(n)]

print(arr)  # [10, 20, 30, 40, 50]

reverse(arr, n)

# arr = arr[::-1] # creates a reversed copy of the given list and return it
# arr.reverse()  # reverses the list in-place

# arr = list(reversed(arr))  # creates a reversed copy of the given list and returns it

print(arr)  # [50, 40, 30, 20, 10]
