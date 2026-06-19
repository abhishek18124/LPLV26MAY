n = int(input())
arr = [int(input()) for _ in range(n)]

f_msf = float("-inf")
s_msf = float("-inf")
t_msf = float("-inf")

# time : O(n)

for num in arr:
    if num > f_msf:
        t_msf = s_msf
        s_msf = f_msf
        f_msf = num
    elif num > s_msf:
        t_msf = s_msf
        s_msf = num
    elif num > t_msf:
        t_msf = num

print(f_msf, s_msf, t_msf)
