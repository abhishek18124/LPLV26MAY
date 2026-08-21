def nsr(arr: list[int]) -> list[int]:
    stk = []  # monotonic stack # tracks indices
    ans = []
    n = len(arr)
    for i in range(n - 1, -1, -1):
        # find the index of nearest smaller element to the right of arr[i]
        while stk and arr[stk[-1]] >= arr[i]:
            stk.pop()

        if not stk:
            # there is no smaller element to the right of arr[i]
            ans.append(n)
        else:
            # whatever is at the top of the stack is the index of the nearest smaller element to the right of arr[i]
            ans.append(stk[-1])

        stk.append(i)

    ans.reverse()

    return ans


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
nsr_idx = nsr(arr)  # O(n)
nsl_idx = nsl(arr)  # O(n)

max_so_far = 0

for i in range(len(arr)):  # O(n)
    hgt = arr[i]
    best_width = nsr_idx[i] - nsl_idx[i] - 1
    best_area = hgt * best_width
    max_so_far = max(max_so_far, best_area)

print(max_so_far)

# time : O(n)
# space: O(n) due to monotonic stacks used in nsl and nsr fn
