pairs = [(3, 1), (2, 0), (1, 3), (4, 2)]
# sorted_pairs = sorted(pairs)
sorted_pairs = sorted(pairs, key=lambda p: p[1], reverse=True)
print(sorted_pairs)
