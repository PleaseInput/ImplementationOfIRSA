"""
-1. get frequence table
-2. get heap nodes
-3. merge the heap to a tree
-4. get code and reverseCode
5. encode
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
    def __init__(self):
        self.HCInputText = ""
        self.frequence = {}
        self.heapNodes = []
        self.code = {}
        self.reverseCode = {}
        self.HCOutputText = ""

    def getFrequence(self):
        for chr in self.HCInputText:
            if not chr in self.frequence:
                self.frequence[chr] = self.HCInputText.count(chr)

    def getHeapNodes(self):
        for chr in self.frequence:
            heapNode = HeapNode(chr, self.frequence[chr])
            heapq.heappush(self.heapNodes, heapNode)

    def mergeHeapNodes(self):
        while len(self.heapNodes) > 1:
            tmpNode0 = heapq.heappop(self.heapNodes)
            tmpNode1 = heapq.heappop(self.heapNodes)
            newNode = HeapNode(None, tmpNode0.freq + tmpNode1.freq)
            newNode.leftChild = tmpNode0
            newNode.rightChild = tmpNode1
            heapq.heappush(self.heapNodes, newNode)

    def getCode(self):
        root = heapq.heappop(self.heapNodes)
        if root == None:
            return

        currentCode = ""
        self.getCodeRecursively(root, currentCode)

    def getCodeRecursively(self, root, currentCode):
        # not leaf
        if root.chr == None:
            self.getCodeRecursively(root.leftChild, currentCode + "0")
            self.getCodeRecursively(root.rightChild, currentCode + "1")
            return

        # leaf
        self.code[root.chr] = currentCode
        self.reverseCode[currentCode] = root.chr

    # encoded text: e.g. a->010
    def getEncodedText(self):
        for chr in self.HCInputText:
            self.HCOutputText += self.code[chr]

    # compress text: e.g. apple->cm
    def compressText(self, HCInputText = ""):
        self.HCInputText = HCInputText
        self.getFrequence()
        self.getHeapNodes()
        self.mergeHeapNodes()
        self.getCode()
        self.getEncodedText()

def main():
    inputText = "apple"
    hc = HuffmanCoding()
    hc.compressText(inputText)
    print("hi")

main()