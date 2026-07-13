nums = [[10, 20], [30, 40], [50, 60]]
print(nums)

# print(nums[0][0])
# print(nums[0][1])
# print(nums[1][0])
# print(nums[1][1])
# print(nums[2][0])
# print(nums[2][1])

# m = 3
m = len(nums)

# for i in range(m):
#     # print the ith row
#     print(nums[i][0])
#     print(nums[i][1])

# n = 2
n = len(nums[0])

# for i in range(m):
#     # print the ith row
#     for j in range(n):
#         print(nums[i][j])

for i in range(m):
    # print the ith row
    for j in range(n):
        print(nums[i][j], end=" ")
    print()
