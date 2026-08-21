# time : O(n)
# space: O(n) due to monotonic stack
def ngl(arr: list[int]) -> list[int]:
    stk = []  # monotonic stack
    ans = []
    n = len(arr)
    for i in range(n):
        # find the nearest greater element to the left of arr[i]
        while stk and stk[-1] <= arr[i]:
            stk.pop()

        if not stk:
            # there is no greater element to the left of arr[i]
            ans.append(-1)
        else:
            # whatever is at the top of the stack is the nearest greater element to the left of arr[i]
            ans.append(stk[-1])

        stk.append(arr[i])

    return ans


arr = list(map(int, input().split()))
ans = ngl(arr)
print(ans)
