num = int(input())
s = 0

while num != 0:
    d = num % 10
    s = s + num % 10
    num = num // 10

print(s)
