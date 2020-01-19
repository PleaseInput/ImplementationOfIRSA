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
        if other == None:
            return -1
        if not isinstance(other, HeapNode):
            return -1
        return self.freq < other.freq
        
class HuffmanCoding:

    def __init__(self, textBeforeHC):
        if textBeforeHC is None:
            print('Input is None'); return
        if not isinstance(textBeforeHC, str):
            print('Input is not str'); return
        if textBeforeHC == '':
            print('Input is empty'); return

        self.textBeforeHC = textBeforeHC

    def getFrequence(self):
        frequence = {}
        for chr in self.textBeforeHC:
            if not chr in frequence:
                frequence[chr] = self.textBeforeHC.count(chr)

        return frequence

    def getHeapNodes(self, frequence):
        heapNodes = []
        for chr in frequence:
            heapNode = HeapNode(chr, frequence[chr])
            heapq.heappush(heapNodes, heapNode)

        return heapNodes

    def mergeHeapNodes(self, heapNodes):
        while len(heapNodes) > 1:
            tmpNode0 = heapq.heappop(heapNodes)
            tmpNode1 = heapq.heappop(heapNodes)
            newNode = HeapNode(None, tmpNode0.freq + tmpNode1.freq)
            newNode.leftChild = tmpNode0
            newNode.rightChild = tmpNode1
            heapq.heappush(heapNodes, newNode)

        return heapq.heappop(heapNodes)

    def getCode(self, root):
        if root == None:
            assert False; return

        currentCode = ""
        code = {}
        reversedCode = {}
        self.getCodeRecursively(root, currentCode, code, reversedCode)

        return code, reversedCode

    def getCodeRecursively(self, root, currentCode, code, reversedCode):
        # not leaf
        if root.chr == None:
            self.getCodeRecursively(root.leftChild, currentCode + "0", code, reversedCode)
            self.getCodeRecursively(root.rightChild, currentCode + "1", code, reversedCode)
            return

        # leaf
        code[root.chr] = currentCode
        reversedCode[currentCode] = root.chr

    # encoded text: e.g. app->011
    def getEncodedText(self, code):
        textAfterHC = ''
        for chr in self.textBeforeHC:
            textAfterHC += code[chr]

        return textAfterHC

    # compress text: e.g. apple->cm
    def compressText(self):
        frequence = self.getFrequence()
        heapNodes = self.getHeapNodes(frequence)
        root = self.mergeHeapNodes(heapNodes)
        code, reversedCode = self.getCode(root)
        textAfterHC = self.getEncodedText(code)
        
        return reversedCode, textAfterHC

    # decompress text
    def decompressText(self, reversedCode, textAfterHC):
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
    reversedCode, textAfterHC = hc.compressText()
    textBeforeHC = hc.decompressText(reversedCode, textAfterHC)

    print(testText == textBeforeHC)
main()