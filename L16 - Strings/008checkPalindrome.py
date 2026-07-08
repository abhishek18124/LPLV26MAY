# time : n/2.const ~ O(n)
# space: O(1)


def isPalindrome(s: str) -> bool:
    n = len(s)
    i, j = 0, n - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            # s is not a palindrome
            return False

    # s is a palindrome
    return True


s = input()
# if isPalindrome(s):
#     print("palindrome")
# else:
#     print("not a palindrome")

print("palindrome") if isPalindrome(s) else print("not a palindrome")
