s = "coding"
print(len(s))
print(s[0])
print(s[5], s[-1])
print(s[0:3], s[:3])
print(s[4:])

# s[0] = "x" # TypeError : str object does not support item assignment

x = 10
print(type(x))
y = str(x)
print(type(y))
print(y)

z = 3.14
print(type(z))
y = str(z)
print(type(y))
print(y)

word = "india"
for ch in word:
    print(ch)

i = 0
while i < len(word):
    print(word[i])
    i += 1
