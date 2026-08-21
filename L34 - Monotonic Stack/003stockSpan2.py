# time : O(n)
# space: O(n) due to monotonic stack
def stock_span(arr: list[int]) -> list[int]:
    stk = []  # monotonic stack # each element is an integer (index)
    ans = []  # to store the stock span
    n = len(arr)
    for i in range(n):
        # find the index of nearest greater element to the left of arr[i]
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        if not stk:
            # there is no greater element to the left of arr[i]
            j = -1
        else:
            # whatever is at the top of the stack is the nearest greater element to the left of arr[i]
            j = stk[-1]

        ans.append(i - j)

        stk.append(i)

    return ans


arr = list(map(int, input().split()))
ans = stock_span(arr)
print(ans)
