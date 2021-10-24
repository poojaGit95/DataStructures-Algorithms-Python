class BinaryTreeList:
    def __init__(self, maxsize):
        self.blist = maxsize*[None]
        self.lastindex = 0
        self.maxsize = maxsize

    def insertElement(self, value):
        if( self.maxsize == self.lastindex+1):
            return "tree full"
        else:
            self.blist[self.lastindex+1] = value
            self.lastindex+=1
            return "value inserted"

    def preOrderTraversal(self,index):
        if index>self.lastindex:
            return "no elements"
        else:
            print(self.blist[index])
            self.preOrderTraversal(index*2)
            self.preOrderTraversal((index*2)+1)

    def levelOrderTraversal(self):
        if self.lastindex==0:
            return"no elements"
        else:
            for i in range(1,self.lastindex+1):
                print(self.blist[i])

    def searchElement(self, value):
        if self.lastindex==0:
            return"no elements"
        else:
            for i in range(1,self.lastindex+1):
                if self.blist[i]==value:
                    return "found"
            return "not found"

    def deleteElement(self,value):
        if self.lastindex==0:
            return"no elements"
        else:
            for i in range(1,self.lastindex+1):
                if self.blist[i]==value:
                    self.blist[i] = self.blist[self.lastindex]
                    self.blist[self.lastindex] = None
                    self.lastindex-=1
                    return "deleted"
            return "failed"

    def deleteTree(self):
        self.blist = None
        self.lastindex=0



btree = BinaryTreeList(5)
btree.insertElement("Drinks")
btree.insertElement("hot")
btree.insertElement("cold")
btree.preOrderTraversal(1)
print("-------")
print(btree.searchElement("drink"))
print(btree.deleteElement("Drinks"))
btree.levelOrderTraversal()
print("-----------")
btree.deleteTree()
btree.levelOrderTraversal()

