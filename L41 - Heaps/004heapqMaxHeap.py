import heapq

v = []

heapq.heappush(v, -3)
heapq.heappush(v, -2)
heapq.heappush(v, -4)
heapq.heappush(v, -5)
heapq.heappush(v, -1)


while v:
    print(-heapq.heappop(v))
