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

    def insert(self, value, frequency=None):
        if frequency is None:
            self.elements.append(value)
        else:
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

    def tree_conversion(self):
        while 1 < self.size:
            left = self.extract_min()
            right = self.extract_min()
            node = MinHeapNode(None, left.frequency + right.frequency)
            node.left = left
            node.right = right
            self.insert(node)

    def get_tree_size(self):
        if 0 == self.size:
            return 0
        return self.get_size_from(self.elements[0])

    def get_size_from(self, node):
        if node.left is None:
            return 0
        else:
            return 1 + self.get_size_from(node.left) + self.get_size_from(node.right)

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
