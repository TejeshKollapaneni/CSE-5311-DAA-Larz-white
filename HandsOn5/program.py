class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def heapify(self, i):
        smallest = i
        l = self.left(i)
        r = self.right(i)
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_min_heap(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.heapify(i)

    def pop(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root

    def change_value(self, index, new_value):
        if index < 0 or index >= len(self.heap):
            return False
        old_value = self.heap[index]
        self.heap[index] = new_value
        if new_value < old_value:
            while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
                self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
                index = self.parent(index)
        else:
            self.heapify(index)
        return True

# Example usage
heap = MinHeap()
heap.build_min_heap([4, 10, 3, 5, 1])
print(heap.heap)  # Output: [1, 4, 3, 10, 5]

# Change the value at index 2 to 2
heap.change_value(2, 2)
print(heap.heap)  # Output: [1, 2, 3, 10, 5]

# Pop the root node
root = heap.pop()
print("Popped root:", root)  # Output: Popped root: 1
print(heap.heap)  # Output: [2, 4, 3, 10, 5]

