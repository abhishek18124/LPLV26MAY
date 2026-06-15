# def isEven(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# def isEven(n):
#     if n % 2 == 0:
#         return True

#     return False


# def isEven(n):
#     return True if n % 2 == 0 else False


def isEven(n: int) -> bool:
    return n % 2 == 0


# ans = isEven(4)
# print(ans)

# print(isEven(5))

num = int(input())

if isEven(num):
    print(str(num) + " is even")
else:
    print(str(num) + " is odd")
