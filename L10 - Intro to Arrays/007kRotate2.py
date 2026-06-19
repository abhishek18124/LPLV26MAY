class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k = k % n

        def reverse(i: int, j: int) -> None:
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
