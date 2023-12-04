class MaxHeap:
    def __init__(self, n):
        # Initializes an empty heap list
        self.heap = []  
        self.stock_num = n

    def insert(self, stock):
        # Inserts a new stock into the heap and then heapifies up
        self.heap.append(stock)
        self._heapify_up(len(self.heap) - 1)

    def get_heap(self):
        # Returns the entire heap
        return self.heap

    def extract_max(self):
        # Removes and returns the maximum value from the heap, then heapifies down
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def top_stocks(self):
        # Returns the top n stocks from the heap without altering the original heap
        temp_heap = self.heap.copy()
        top_stocks = []
        for _ in range(self.stock_num):
            if not self.heap:
                break
            top_stocks.append(self.extract_max())
        self.heap = temp_heap
        return top_stocks

    def _heapify_up(self, index):
        # Ensures the heap property is maintained after insertion
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        # Ensures the heap property is maintained after extraction
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

class MinHeap:
    def __init__(self, n):
        # Initializes an empty heap list
        self.heap = []
        self.stock_num = n 
    def insert(self, stock):
        # Inserts a new stock into the heap and then heapifies up
        self.heap.append(stock)
        self._heapify_up(len(self.heap) - 1)

    def get_heap(self):
        # Returns the entire heap
        return self.heap

    def extract_min(self):
        # Removes and returns the minimum value from the heap, then heapifies down.
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value

    def top_stocks(self):
        # Returns the top n stocks from the heap without altering the original heap
        temp_heap = self.heap.copy()
        top_stocks = []
        for _ in range(self.stock_num):
            if not self.heap:
                break
            top_stocks.append(self.extract_min())
        self.heap = temp_heap
        return top_stocks

    def _heapify_up(self, index):
        # Ensures the heap property is maintained after insertion
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        # Ensures the heap property is maintained after extraction
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
