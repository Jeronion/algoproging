class MinHeap:

    def __init__(self):
        self.arr = []

    def left(self, i): 
        return 2 * i + 1

    def right(self, i): 
        return 2 * i + 2

    def parent(self, i): 
        return (i - 1) // 2

    def get_min(self):
        return self.arr[0] if self.arr else None

    def insert(self, k):
        self.arr.append(k)
        i = len(self.arr) - 1

        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def decrease_key(self, i, new_val):
        self.arr[i] = new_val

        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def extract_min(self):
        if len(self.arr) <= 0: 
            return None
        if len(self.arr) == 1: 
            return self.arr.pop()

        res = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.min_heapify(0)
        return res

    def delete_key(self, i):
        self.decrease_key(i, -float('inf'))
        self.extract_min()

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        n = len(self.arr)

        smallest = i

        if l < n and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < n and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)