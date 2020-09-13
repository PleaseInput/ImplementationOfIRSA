"""
Input: a string. e.g. 'app'.
Output: a header(reversedCode) and a binary string. e.g. a0p1, 011.
-1. get frequence table
-2. get heap nodes
-3. merge the heap to a tree
-4. get code and reversedCode
-5. encode
"""
import heapq


class HeapNode:
    def __init__(self, chr, freq):
        self.chr = chr
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

    def __init__(self, textBeforeHC):
        if textBeforeHC is None:
            print('Input is None')
            return
        if not isinstance(textBeforeHC, str):
            print('Input is not str')
            return
        if textBeforeHC == '':
            print('Input is empty')
            return

        self.textBeforeHC = textBeforeHC

    def _get_frequence(self):
        frequence = {}
        for chr in self.textBeforeHC:
            if not chr in frequence:
                frequence[chr] = self.textBeforeHC.count(chr)

        return frequence

    def _get_heap_nodes(self, frequence):
        heapNodes = []
        for chr in frequence:
            heapNode = HeapNode(chr, frequence[chr])
            heapq.heappush(heapNodes, heapNode)

        return heapNodes

    def _merge_heap_nodes(self, heapNodes):
        while len(heapNodes) > 1:
            tmpNode0 = heapq.heappop(heapNodes)
            tmpNode1 = heapq.heappop(heapNodes)
            newNode = HeapNode(None, tmpNode0.freq + tmpNode1.freq)
            newNode.leftChild = tmpNode0
            newNode.rightChild = tmpNode1
            heapq.heappush(heapNodes, newNode)

        return heapq.heappop(heapNodes)

    def _get_code(self, root):
        if root == None:
            assert False
            return

        currentCode = ""
        code = {}
        reversedCode = {}
        self._get_code_recursively(root, currentCode, code, reversedCode)

        return code, reversedCode

    def _get_code_recursively(self, root, currentCode, code, reversedCode):
        # not leaf
        if root.chr == None:
            self._get_code_recursively(root.leftChild, currentCode + "0", code, reversedCode)
            self._get_code_recursively(root.rightChild, currentCode + "1", code, reversedCode)
            return

        # leaf
        code[root.chr] = currentCode
        reversedCode[currentCode] = root.chr

    # encoded text: e.g. app->011
    def _get_encoded_text(self, code):
        textAfterHC = ''
        for chr in self.textBeforeHC:
            textAfterHC += code[chr]

        return textAfterHC

    # compress text: e.g. apple->cm
    def compress_text(self):
        frequence = self._get_frequence()
        heapNodes = self._get_heap_nodes(frequence)
        root = self._merge_heap_nodes(heapNodes)
        code, reversedCode = self._get_code(root)
        textAfterHC = self._get_encoded_text(code)

        return reversedCode, textAfterHC

    # decompress text
    def decompress_text(self, reversedCode, textAfterHC):
        currentCode = ''
        textBeforeHC = ''
        for chr in textAfterHC:
            currentCode += chr
            if currentCode in reversedCode:
                textBeforeHC += reversedCode[currentCode]
                currentCode = ''

        return textBeforeHC

def main():
    testText = "apple"
    hc = HuffmanCoding(testText)
    reversedCode, textAfterHC = hc.compress_text()
    textBeforeHC = hc.decompress_text(reversedCode, textAfterHC)

    print(testText == textBeforeHC)

if __name__ == "__main__":
    main()
    