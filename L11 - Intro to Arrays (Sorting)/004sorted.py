nums = [30, 10, 20, 50, 40]
sorted_nums = sorted(nums)  # creates a sorted list in inc. order
# sorted_nums = sorted(nums, reverse=True) # creates a sorted list in dec. order

print(nums)
print(sorted_nums)

temp = [87, 90, 95, 76, 98]
# temp.sort() # sorts the list in-place
temp.sort(reverse=True)
print(temp)

animals = ["ch", "ze", "al", "be", "ti"]
sorted_animals = sorted(animals)
# sorted_animals = sorted(animals, reverse=True)
print(sorted_animals)

names = ["ifrah", "aryan", "avi", "aditya", "yash"]
sorted_names = sorted(names, key=len)
# sorted_names = sorted(names, key=len, reverse=True)
print(sorted_names)
