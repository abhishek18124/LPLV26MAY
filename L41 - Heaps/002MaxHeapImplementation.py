class max_heap:
    def __init__(self):
        self.v = []  # array representation of the max-heap

    # Insert an element and restore the max-heap
    # property by moving the element upwards.
    def push(self, val):
        self.v.append(val)
        child_idx = len(self.v) - 1
        parent_idx = (child_idx - 1) // 2
        while child_idx != 0 and self.v[child_idx] > self.v[parent_idx]:
            self.v[child_idx], self.v[parent_idx] = (
                self.v[parent_idx],
                self.v[child_idx],
            )
            child_idx = parent_idx
            parent_idx = (child_idx - 1) // 2

    # Remove the maximum element (root) and restore the
    # max-heap property by moving the new root downwards.
    def pop(self):
        def sift_down(i):
            max_idx = i
            left_child_idx = 2 * i + 1
            if (
                left_child_idx < len(self.v)
                and self.v[left_child_idx] > self.v[max_idx]
            ):
                max_idx = left_child_idx

            right_child_idx = 2 * i + 2
            if (
                right_child_idx < len(self.v)
                and self.v[right_child_idx] > self.v[max_idx]
            ):
                max_idx = right_child_idx

            if max_idx != i:
                self.v[i], self.v[max_idx] = self.v[max_idx], self.v[i]
                sift_down(max_idx)

        self.v[0], self.v[-1] = self.v[-1], self.v[0]
        self.v.pop()
        sift_down(0)

    # Return the maximum element without removing it.
    def top(self):
        return self.v[0]

    # Return the number of elements in the heap.
    def size(self):
        return len(self.v)

    # Return True if the heap contains no elements.
    def empty(self):
        return len(self.v) == 0


m = max_heap()

m.push(3)
m.push(2)
m.push(4)
m.push(5)
m.push(1)

while not m.empty():
    print(m.top())
    m.pop()
