country_set = {"India", "Russia", "Japan", "France"}
print(type(country_set))
print(len(country_set))

country_list = ["India", "Russia", "India", "Japan"]
country_set = set(country_list)
print(type(country_set))
print(len(country_set))
print(country_set)

s = set()
print(type(s))

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(s)
print(len(s))

s.add(5)

print(s)
print(len(s))

s.remove(5)

print(s)
print(len(s))

# s.remove(6) # KeyError

s.discard(6)
s.discard(2)

print(s)

if 3 in s:
    print("Yes")

if 5 not in s:
    print("Not in s")

l = [7, 8, 9]
s.update(l)

print(s)
