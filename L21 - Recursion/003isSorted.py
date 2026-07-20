def f(x: list[int], i: int) -> bool:
    # base case
    if i == len(x) - 1:
        # f(n-1) : check if x[n-1...n-1] = [x[n-1]] is sorted or not
        return True

    # recursive case

    # f(i) : check if x[i...n-1] is sorted or not

    return x[i] < x[i + 1] and f(x, i + 1)


x = [10, 20, 20, 40, 50]
print("sorted") if f(x, 0) else print("not sorted")
