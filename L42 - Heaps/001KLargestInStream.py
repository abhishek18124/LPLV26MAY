import heapq

k = int(input())

h = []  # internal representation of min_heap

while True:
    val = int(input())
    if val == 0:
        break
    elif val == -1:
        print(h)
    else:
        heapq.heappush(h, val)
        if len(h) > k:
            heapq.heappop(h)
