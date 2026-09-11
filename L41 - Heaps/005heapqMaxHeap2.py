import heapq

v = []

heapq.heappush_max(v, 3)  # heappush_max, heappop_max works py 3.14 onwards
heapq.heappush_max(v, 2)
heapq.heappush_max(v, 4)
heapq.heappush_max(v, 5)
heapq.heappush_max(v, 1)

# while len(v) > 0:
#   print(v[0])
#   heapq.heappop_max(v)


# while v:
#     print(v[0])
#     heapq.heappop_max(v)

while v:
    print(heapq.heappop_max(v))
