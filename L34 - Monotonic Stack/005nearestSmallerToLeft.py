# time : O(n)
# space: O(n) due to monotonic stack
def nsl(arr: list[int]) -> list[int]:
    stk = []  # monotonic stack # tracks indices
    ans = []
    n = len(arr)
    for i in range(n):
        # find the index of nearest smaller element to the left of arr[i]
        while stk and arr[stk[-1]] >= arr[i]:
            stk.pop()

        if not stk:
            # there is no smaller element to the left of arr[i]
            ans.append(-1)
        else:
            # whatever is at the top of the stack is the index of the nearest smaller element to the left of arr[i]
            ans.append(stk[-1])

        stk.append(i)

    return ans


arr = list(map(int, input().split()))
ans = nsl(arr)
print(ans)
