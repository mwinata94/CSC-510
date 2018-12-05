from min_heap import MinHeap
from frequency_list import FrequencyList


class Huffman:
    def __init__(self):
        self.encoding = {}
        self.decoding = {}
        self.decoding_key = ""
        # bit_depth is hardcoded to 8 for now
        self.bit_depth = 8

    def encode(self, data):
        # Create a frequency table
        frequency_list = FrequencyList(data)

        # Initialize the heap
        min_heap = MinHeap()

        # Insert data into the heap
        for key, value in frequency_list.list.items():
            min_heap.insert(key, value)

        # Sort the heap
        min_heap.sort()

        # Convert heap from array to tree
        min_heap.tree_conversion()

        # Populate the code dictionary
        self.parse_heap(min_heap)

        # Return the decoding key + compressed data
        return self.decoding_key + self.compress_data(data)

    def parse_heap(self, heap):
        root = heap.elements[0]
        code = "0"
        self.parse_node(code, root)

    def parse_node(self, code, node):
        if node.value is not None:
            self.decoding_key += bin(ord(node.value))[2:].zfill(self.bit_depth)
            self.encoding[node.value], self.decoding[code] = code, node.value
        else:
            self.decoding_key += "".zfill(self.bit_depth)

        if node.left is not None:
            self.decoding_key += "1"
            self.parse_node(code + "0", node.left)
            self.parse_node(code + "1", node.right)
        else:
            self.decoding_key += "0"

    def compress_data(self, data):
        encoded_data = ""
        for datum in data:
            encoded_data += self.encoding[datum]
        return encoded_data

    def decode(self, data):
        pass
