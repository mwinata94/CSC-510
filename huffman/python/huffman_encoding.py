from min_heap import MinHeap
from frequency_list import FrequencyList


def encode(data):
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

    print(min_heap.get_tree_size())


def decode(data):
    pass
