from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)
q.append(40)
q.append(50)

print(q)

q.popleft()

print(q)

print(q[0])

print(q[-1])

print(len(q))
