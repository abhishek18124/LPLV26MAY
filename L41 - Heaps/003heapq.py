import heapq

v = []

heapq.heappush(v, 3)
heapq.heappush(v, 2)
heapq.heappush(v, 4)
heapq.heappush(v, 5)
heapq.heappush(v, 1)

# while len(v) > 0:
# 	print(v[0])
# 	heapq.heappop(v)


# while v:
#     print(v[0])
#     heapq.heappop(v)

while v:
    print(heapq.heappop(v))
