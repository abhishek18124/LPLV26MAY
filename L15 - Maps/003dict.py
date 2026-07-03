capital_map = {
    "India": "New Delhi",
    "Russia": "Moscow",
    "Japan": "Tokyo",
    "France": "Paris",
}

# print(len(capital_map))
# print(type(capital_map))

# print(capital_map["India"])
# print(capital_map["Japan"])

# if "USA" in capital_map:
#     print(capital_map["USA"])
# else:
#     print("USA not found")

# if "USA" not in capital_map:
#     print("USA not found")
# else:
#     print(capital_map["USA"])

# print(capital_map.get("India"))
# print(capital_map.get("USA"))
# print(capital_map.get("USA", 0))

print(capital_map)
capital_map["USA"] = "Washington"
print(capital_map)
capital_map["Russia"] = "St. Petersberg"
print(capital_map)
del capital_map["France"]
print(capital_map)
if "Spain" in capital_map:
    del capital_map["Spain"]

for k in capital_map:
    print(k)

for k, v in capital_map.items():
    print(k, v)

# list_of_pairs = [
#     ("India", "New Delhi"),
#     ("Russia", "Moscow"),
#     ("Japan", "Tokyo"),
#     ("France", "Paris"),
# ]

# capital_map_2 = dict(list_of_pairs)
# print(type(capital_map_2))
# print(len(capital_map_2))

# d = {}
# print(type(d))

# d = dict()
# print(type(d))
