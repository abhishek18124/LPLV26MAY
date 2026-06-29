def generate_pairs(arr: list[int], n: int) -> None:
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(arr[i], arr[j])
        print()


n = int(input())
arr = list(map(int, input().split()))
generate_pairs(arr, n)
