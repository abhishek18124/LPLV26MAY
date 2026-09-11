class min_heap:
    def __init__(self):
        self.v = []  # array representation of the min-heap

    # Insert an element and restore the min-heap
    # property by moving the element upwards.

    # time : O(logn)
    def push(self, val):
        self.v.append(val)
        child_idx = len(self.v) - 1
        parent_idx = (child_idx - 1) // 2
        while child_idx != 0 and self.v[child_idx] < self.v[parent_idx]:
            self.v[child_idx], self.v[parent_idx] = (
                self.v[parent_idx],
                self.v[child_idx],
            )
            child_idx = parent_idx
            parent_idx = (child_idx - 1) // 2

    # Remove the minimum element (root) and restore the
    # min-heap property by moving the new root downwards.

    # time : O(logn)
    def pop(self):
        # time : O(logn)
        # space : O(logn) due to fn call stack

        # def sift_down(i):
        #     min_idx = i
        #     left_child_idx = 2 * i + 1
        #     if (
        #         left_child_idx < len(self.v)
        #         and self.v[left_child_idx] < self.v[min_idx]
        #     ):
        #         min_idx = left_child_idx

        #     right_child_idx = 2 * i + 2
        #     if (
        #         right_child_idx < len(self.v)
        #         and self.v[right_child_idx] < self.v[min_idx]
        #     ):
        #         min_idx = right_child_idx

        #     if min_idx != i:
        #         self.v[i], self.v[min_idx] = self.v[min_idx], self.v[i]
        #         sift_down(min_idx)

        # time : O(logn)
        # space: O(1)
        def sift_down(i):
            while True:
                min_idx = i
                left_child_idx = 2 * i + 1
                if (
                    left_child_idx < len(self.v)
                    and self.v[left_child_idx] < self.v[min_idx]
                ):
                    min_idx = left_child_idx

                right_child_idx = 2 * i + 2
                if (
                    right_child_idx < len(self.v)
                    and self.v[right_child_idx] < self.v[min_idx]
                ):
                    min_idx = right_child_idx

                if min_idx == i:
                    break
                else:
                    self.v[i], self.v[min_idx] = self.v[min_idx], self.v[i]
                    i = min_idx

        self.v[0], self.v[-1] = self.v[-1], self.v[0]
        self.v.pop()
        sift_down(0)

    # Return the minimum element without removing it.

    # time : O(1)
    def top(self):
        return self.v[0]

    # Return the number of elements in the heap.

    # time : O(1)
    def size(self):
        return len(self.v)

    # Return True if the heap contains no elements.

    # time : O(1)
    def empty(self):
        return len(self.v) == 0


m = min_heap()

m.push(3)
m.push(2)
m.push(4)
m.push(5)
m.push(1)

while not m.empty():
    print(m.top())
    m.pop()
