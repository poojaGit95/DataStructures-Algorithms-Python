class Node:
    def __init__(self, value=None):
        self.nodeValue = value
        self.nodeNext = None

class CircularLL:

    def __init__(self):
        self.head = None
        self.tail = None


    def createList(self):
        node = Node(5)
        node.nodeNext=node
        self.head = node
        self.tail = node

    def insertElement(self, value, location):
        node = Node(value)
        if location==0:
            node.nodeNext = self.head
            self.head = node
            self.tail.nodeNext = node
        elif location==1:
            self.tail.nodeNext = node
            self.tail = node
            node.nodeNext = self.head
        else:
            temp = self.head
            index=0
            while index<location-1:
                temp = temp.nodeNext
                index+=1
            node.nodeNext = temp.nodeNext
            temp.nodeNext = node

    def deleteElement(self, location):
        if self.head==None:
            print("No list present")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head = self.head.nodeNext
                    self.tail.nodeNext = self.head
            elif location==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while temp.nodeNext != self.tail:
                        temp=temp.nodeNext
                    self.tail = temp
                    temp.nodeNext = self.head
            else:
                temp = self.head
                index=0
                while index<location-1:
                    temp = temp.nodeNext
                    index+=1
                nextNode = temp.nodeNext
                temp.nodeNext = nextNode.nodeNext


    def deleteFullList(self):
        self.tail.nodeNext=None
        self.head = None
        self.tail = None

    def displayList(self):
        node = self.head
        while node:
            print(node.nodeValue)
            if(node.nodeNext==self.head):
                return
            node = node.nodeNext
        print ("no elements")



cllist = CircularLL()
cllist.createList()
cllist.insertElement(30,0)
cllist.insertElement(40,0)
cllist.insertElement(20,1)
cllist.insertElement(50,2)
cllist.displayList()
print("-----------------------")
cllist.deleteElement(0)
cllist.displayList()
print("-----------------------")
cllist.deleteFullList()
cllist.displayList()
