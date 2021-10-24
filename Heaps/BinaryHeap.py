class BinaryHeap:
    def __init__(self, size):
        self.hlist = (size+1) * [None]
        self.heapSize = 0
        self.maxsize = size+1

    # return root node i.e. parent
    def peek(self):
        if self.heapSize==0:
            return "no heap"
        else:
            return self.hlist[1]

    def levelOrderTravesal(self):
        if self.heapSize == 0:
            return "no heap"
        else:
            for i in range(1, self.heapSize+1):
                print(self.hlist[i])

    def binaryHeapSize(self):
        return self.heapSize

    def searchElement(self, value):
        if self.heapSize == 0:
            return "no heap"
        else:
            for i in range(1, self.heapSize+1):
                if self.hlist[i] == value:
                    return "found"
            return "not found"

    def heapifyInsert(self,index,heapType):
        if index<=1:
            return
        parentIndex = int(index/2)
        if heapType=="Min":
            if self.hlist[index]<self.hlist[parentIndex]:
                temp = self.hlist[index]
                self.hlist[index] = self.hlist[parentIndex]
                self.hlist[parentIndex] = temp
            self.heapifyInsert(parentIndex, heapType)
        else:
            if self.hlist[index] > self.hlist[parentIndex]:
                temp = self.hlist[index]
                self.hlist[index] = self.hlist[parentIndex]
                self.hlist[parentIndex] = temp
            self.heapifyInsert(parentIndex, heapType)


    def insertElement(self, element, heapType):
        if self.heapSize+1 == self.maxsize:
            return "heap is full"
        else:
            self.hlist[self.heapSize+1]=element
            self.heapSize+=1
            self.heapifyInsert(self.heapSize,heapType)

    def heapifyDelete(self,index,heapType):
        leftIndex = index*2
        rightIndex = (index*2) + 1
        swapChild = 0

        if self.heapSize<leftIndex:
            return
        elif self.heapSize==leftIndex:
            if heapType=="Min":
                if self.hlist[index]>self.hlist[leftIndex]:
                    temp = self.hlist[index]
                    self.hlist[index] = self.hlist[leftIndex]
                    self.hlist[leftIndex] = temp
                return
            else:
                if self.hlist[index]<self.hlist[leftIndex]:
                    temp = self.hlist[index]
                    self.hlist[index] = self.hlist[leftIndex]
                    self.hlist[leftIndex] = temp
                return
        else:
            if heapType=="Min":
                if self.hlist[leftIndex]<self.hlist[rightIndex]:
                    swapChild=leftIndex
                else:
                    swapChild=rightIndex
                if self.hlist[index] > self.hlist[swapChild]:
                    temp = self.hlist[index]
                    self.hlist[index] = self.hlist[leftIndex]
                    self.hlist[leftIndex] = temp
            else:
                if self.hlist[leftIndex]>self.hlist[rightIndex]:
                    swapChild=leftIndex
                else:
                    swapChild=rightIndex
                if self.hlist[index] < self.hlist[swapChild]:
                    temp = self.hlist[index]
                    self.hlist[index] = self.hlist[leftIndex]
                    self.hlist[leftIndex] = temp
            self.heapifyDelete(swapChild,heapType)


    def extractRoot(self):
        if self.heapSize==0:
            return "no heap"
        else:
            self.hlist[1]=self.hlist[self.heapSize]
            self.hlist[self.heapSize]=None
            self.heapSize-=1
            self.heapifyDelete(1,"Min")



heap = BinaryHeap(5)
print(heap.peek())
print(heap.binaryHeapSize())
heap.insertElement(1,"Min")
heap.insertElement(4,"Min")
heap.insertElement(30,"Min")
heap.insertElement(40,"Min")
heap.levelOrderTravesal()
print("-------------")
heap.extractRoot()
heap.levelOrderTravesal()


