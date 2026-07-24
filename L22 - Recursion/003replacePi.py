# time : O(n)
# space: O(n) due to fn call stack


def f(arr: list[str], i: int, out: list[str]) -> None:
    # base case

    if i == len(arr) - 1:
        out.append(arr[i])
        return

    if i == len(arr):
        return

    # recursive case

    # f(i) : replace all the "pi" with "3.14" in arr[i...len(arr)-1]

    if arr[i] == "p" and arr[i + 1] == "i":
        out.extend(list("3.14"))
        f(arr, i + 2, out)
    else:
        out.append(arr[i])
        f(arr, i + 1, out)


arr = list(input())
out = []
f(arr, 0, out)
print("".join(out))
