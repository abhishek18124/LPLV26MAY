# time : O(n^3)
def generate_subarrays(arr: list[int], n: int) -> None:
    for i in range(n):
        for j in range(i, n):
            # print the subarray that
            # starts at the ith index
            # and ends at the jth idx

            # print(arr[i:j+1])

            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()


n = int(input())
arr = list(map(int, input().split()))
generate_subarrays(arr, n)
