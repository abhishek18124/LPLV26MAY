s = "the sun rises in the east and the sun sets in the west"
print(s.find("sun"))
print(s.find("in"))
print(s.rfind("in"))
print(s.find("moon"))

# t = s.replace("sun", "moon")
t = s.replace("sun", "")
print(s)
print(t)

x = "   hi today is 8th july   "
print(x)
# y = x.strip()
# y = x.lstrip()
y = x.rstrip()
print(y)
