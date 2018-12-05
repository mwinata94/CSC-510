from huffman import Huffman


def main():
    test = "test test teswqu4598qyw69n7wbiwugnvniauet"
    print(test)

    huffman1 = Huffman()
    compressed = huffman1.encode(test)
    print(compressed)

    # reset values to test decoder
    huffman2 = Huffman()
    uncompressed = huffman2.decode(compressed)
    print(uncompressed)


if __name__ == '__main__':
    main()
