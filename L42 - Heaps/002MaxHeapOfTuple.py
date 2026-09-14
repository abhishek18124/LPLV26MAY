import heapq

h = []  # internal representation of max_heap

heapq.heappush(h, (-5, -2))
heapq.heappush(h, (-6, -1))
heapq.heappush(h, (-3, -2))
heapq.heappush(h, (-5, -4))
heapq.heappush(h, (-4, -2))

while h:
    a, b = heapq.heappop(h)
    print(-a, -b)
