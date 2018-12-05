from min_heap_node import MinHeapNode


class MinHeap:
    def __init__(self):
        self.elements = []
        self.size = 0

    def __str__(self):
        temp = "%-20s : %30s\n" % ("index", "node")
        for i, node in enumerate(self.elements):
            temp += "%-20s : %30s\n" % (i, str(node))
        return temp

    def insert(self, value, frequency):
        self.elements.append(MinHeapNode(value, frequency))
        self.size += 1
        i = self.size - 1
        parent = self.parent(i)
        while 0 != i and self.elements[parent] > self.elements[i]:
            self.swap(i, parent)
            i = parent
            parent = self.parent(i)

    def extract_min(self):
        if 0 == self.size:
            return None
        elif 1 == self.size:
            temp = self.elements.pop()
            self.size -= 1
            return temp
        else:
            temp = self.elements[0]
            self.elements[0] = self.elements.pop()
            self.size -= 1
            self.min_heapify(self.size, 0)
            return temp

    def min_heapify(self, size, i):
        left = self.left(i)
        right = self.right(i)
        largest = i
        if left < size and self.elements[left] > self.elements[i]:
                largest = left
        if right < size and self.elements[right] > self.elements[largest]:
                largest = right
        if largest != i:
            self.swap(i, largest)
            self.min_heapify(size, largest)

    def swap(self, a, b):
        self.elements[a].value, self.elements[b].value = self.elements[b].value, self.elements[a].value
        self.elements[a].frequency, self.elements[b].frequency = self.elements[b].frequency, self.elements[a].frequency

    def sort(self):
        for i in range(self.size, -1, -1):
            self.min_heapify(self.size, i)
        for i in range(self.size - 1, 0, -1):
            self.swap(0, i)
            self.min_heapify(i, 0)

    @staticmethod
    def parent(i):
        if i:
            return int((i - 1) / 2)
        else:
            return i

    @staticmethod
    def left(i):
        return int((i * 2) + 1)

    @staticmethod
    def right(i):
        return int((i * 2) + 2)
