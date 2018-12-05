class MinHeapNode:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

    def __str__(self):
        return "%-10s : %10s " % (self.value, self.frequency)

    def __lt__(self, node):
        return self.frequency < node.frequency

    def __eq__(self, node):
        return self.frequency == node.frequency
