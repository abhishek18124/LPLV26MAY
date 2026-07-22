# time : O(n^2)
# space: O(n) due to fn call stack


def f(arr: list[str], i: int) -> None:
    # base case

    # if i == len(arr) - 1:
    #     return

    # if i == len(arr):
    #     return

    if i >= len(arr) - 1:
        return

    # recursive case

    # f(i) : replace all the "pi" with "3.14" in arr[i...len(arr)-1]

    if arr[i] == "p" and arr[i + 1] == "i":
        arr[i : i + 2] = list("3.14")
        f(arr, i + 4)
    else:
        f(arr, i + 1)


arr = list(input())
print(arr)
f(arr, 0)
print(arr)
print("".join(arr))
