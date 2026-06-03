n = 5
for i in range(n):
    print(i)
print("You are outside the for-loop")

for i in range(2, n):
    print(i)
print("You are outside the for-loop")

n = 10

for i in range(1, n, 2):
    print(i)
print("You are outside the for-loop")

n = 5

for i in range(n, 0, -1):  # [n, 0)
    print(i)
print("You are outside the for-loop")
