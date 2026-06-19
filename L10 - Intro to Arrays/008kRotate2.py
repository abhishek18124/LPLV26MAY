arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(arr)

arr.reverse()
arr[:k] = arr[:k][::-1]
arr[k:] = arr[k:][::-1]

print(arr)
