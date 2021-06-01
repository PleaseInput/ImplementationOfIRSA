"""
Input: a string. e.g. 'app'.
Output: a header(reversedCode) and a binary string. e.g. a0p1, 011.
-1. get frequency table
-2. get heap nodes
-3. merge the heap to a tree
-4. get code and reversedCode
-5. encode
"""
import heapq


class HeapNode:
    def __init__(self, char, freq):
        self.chr = char
        self.freq = freq
        self.leftChild = None
        self.rightChild = None

    # __cmp__ has gone since python 3
    def __lt__(self, other):
        if other is None:
            return -1
        if not isinstance(other, HeapNode):
            return -1
        return self.freq < other.freq


class HuffmanCoding:

    def __init__(self, text_before_coding):
        if text_before_coding is None:
            print('Input is None')
            return
        if not isinstance(text_before_coding, str):
            print('Input is not str')
            return
        if text_before_coding == '':
            print('Input is empty')
            return

        self.textBeforeHC = text_before_coding

    def _get_frequency(self):
        frequency = {}
        for char in self.textBeforeHC:
            if char not in frequency:
                frequency[char] = self.textBeforeHC.count(char)

        return frequency

    @staticmethod
    def _get_heap_nodes(frequency):
        heap_nodes = []
        for char in frequency:
            heap_node = HeapNode(char, frequency[char])
            heapq.heappush(heap_nodes, heap_node)

        return heap_nodes

    @staticmethod
    def _merge_heap_nodes(heap_nodes):
        while len(heap_nodes) > 1:
            tmp_node0 = heapq.heappop(heap_nodes)
            tmp_node1 = heapq.heappop(heap_nodes)
            new_node = HeapNode(None, tmp_node0.freq + tmp_node1.freq)
            new_node.leftChild = tmp_node0
            new_node.rightChild = tmp_node1
            heapq.heappush(heap_nodes, new_node)

        return heapq.heappop(heap_nodes)

    def _get_code(self, root):
        if root is None:
            assert False

        current_code = ""
        code = {}
        reversed_code = {}
        self._get_code_recursively(root, current_code, code, reversed_code)

        return code, reversed_code

    def _get_code_recursively(self, root, current_code, code, reversed_code):
        # not leaf
        if root.chr is None:
            self._get_code_recursively(root.leftChild, current_code + "0", code, reversed_code)
            self._get_code_recursively(root.rightChild, current_code + "1", code, reversed_code)
            return

        # leaf
        code[root.chr] = current_code
        reversed_code[current_code] = root.chr

    # encoded text: e.g. app->011
    def _get_encoded_text(self, code):
        text_after_huffman_coding = ''
        for char in self.textBeforeHC:
            text_after_huffman_coding += code[char]

        return text_after_huffman_coding

    # compress text: e.g. apple->cm
    def compress_text(self):
        frequency = self._get_frequency()
        heap_nodes = self._get_heap_nodes(frequency)
        root = self._merge_heap_nodes(heap_nodes)
        code, reversed_code = self._get_code(root)
        text_after_huffman_coding = self._get_encoded_text(code)

        return reversed_code, text_after_huffman_coding

    # decompress text
    @staticmethod
    def decompress_text(reversed_code, text_after_huffman_coding):
        current_code = ''
        text_before_huffman_coding = ''
        for char in text_after_huffman_coding:
            current_code += char
            if current_code in reversed_code:
                text_before_huffman_coding += reversed_code[current_code]
                current_code = ''

        return text_before_huffman_coding


def main():
    test_text = "apple"
    hc = HuffmanCoding(test_text)
    reversed_code, text_after_huffman_coding = hc.compress_text()
    text_before_huffman_coding = hc.decompress_text(reversed_code, text_after_huffman_coding)

    print(test_text == text_before_huffman_coding)


if __name__ == "__main__":
    main()
