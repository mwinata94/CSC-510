from min_heap import MinHeap
from frequency_list import FrequencyList


def main():
    frequency_list = FrequencyList("test test teswqu4598qyw69n7wbiwugnvniauet")
    min_heap = MinHeap()
    for key, value in frequency_list.list.items():
        min_heap.insert(key, value)
    min_heap.sort()
    print(min_heap)


if __name__ == '__main__':
    main()
