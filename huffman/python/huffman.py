from min_heap import MinHeap
from frequency_list import FrequencyList


class Huffman:
    def __init__(self):
        self.data = ""
        self.encoding = {}
        self.decoding = {}
        self.decoding_key = ""
        # bit_depth is hardcoded to 8 for now
        self.bit_depth = 8

    def encode(self, data):
        # Store data
        self.data = data

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
        return self.decoding_key + self.compress_data()

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

    def compress_data(self):
        encoded_data = ""
        for datum in self.data:
            encoded_data += self.encoding[datum]
        return encoded_data

    def decode(self, data):
        # Store data
        self.data = data

        # Populate the code dictionary
        self.parse_code()

        # Return the uncompressed data
        return self.uncompress_data()

    def parse_code(self):
        code = "0"
        self.parse_bits(code)
        empty = "".zfill(self.bit_depth)
        for key in list(self.decoding.keys()):
            if empty == self.decoding[key]:
                # Remove empty decode
                del self.decoding[key]

    def parse_bits(self, code):
        self.decoding[code] = self.data[0:8]
        # Cut out the key
        self.data = self.data[self.bit_depth:]
        child = self.data[0]
        self.data = self.data[1:]
        if "1" == child:
            self.parse_bits(code + "0")
            self.parse_bits(code + "1")

    def uncompress_data(self):
        uncompress_data = ""
        key = ""
        size = len(self.data)
        while size:
            key += self.data[0]
            self.data = self.data[1:]
            if key in self.decoding:
                uncompress_data += self.decoding[key]
                key = ""
            size -= 1
        data = int(uncompress_data, 2)
        return data.to_bytes((data.bit_length() + 7) // 8, 'big').decode()
