# time : O(n)
# space: O(n) due to monotonic stack
def ngr(arr: list[int]) -> list[int]:
    stk = []  # monotonic stack
    ans = []
    n = len(arr)
    for i in range(n - 1, -1, -1):
        # find the nearest greater element to the right of arr[i]
        while stk and stk[-1] <= arr[i]:
            stk.pop()

        if not stk:
            # there is no greater element to the right of arr[i]
            ans.append(-1)
        else:
            # whatever is at the top of the stack is the nearest greater element to the right of arr[i]
            ans.append(stk[-1])

        stk.append(arr[i])

    ans.reverse()

    return ans


arr = list(map(int, input().split()))
ans = ngr(arr)
print(ans)
