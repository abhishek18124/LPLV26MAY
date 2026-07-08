s1 = "abc"
s2 = "z"

if s1 == s2:
    print(s1, " == ", s2)
elif s1 < s2:
    print(s1, " < ", s2)
else:
    print(s1, " > ", s2)

s3 = "xyz"
s4 = s3[:]
print(s3)
print(s4)

s = "abc"
c = s[::-1]
print(s)
print(c)
