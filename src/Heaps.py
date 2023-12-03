class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = []

    def push(self, stock):
        heapq.heappush(self.heap, (-stock[1], stock[0]))
        if len(self.heap) > self.max_size:
            heapq.heappop(self.heap)

    def pop(self):
        if self.heap:
            return (-heapq.heappop(self.heap)[0], self.heap[0][1])
        else:
            raise IndexError("pop from an empty heap")

    def peek(self):
        if self.heap:
            return (-self.heap[0][0], self.heap[0][1])
        else:
            return None

    def get_heap(self):
        return self.heap

    def print_heap(self):
        print("Values in the max-heap:")
        for value, name in self.heap:
            print(f"Name: {name}, Value: {-value}")


class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = []

    def push(self, stock):
        heapq.heappush(self.heap, (stock[1], stock[0]))
        if len(self.heap) > self.max_size:
            heapq.heappop(self.heap)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            raise IndexError("pop from an empty heap")

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def get_heap(self):
        return self.heap

    def print_heap(self):
        print("Values in the min-heap:")
        for value, name in self.heap:
            print(f"Name: {name}, Value: {value}")
