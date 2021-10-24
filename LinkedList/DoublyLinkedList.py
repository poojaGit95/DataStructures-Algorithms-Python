class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.nodeValue = value


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def createList(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    def insertElement(self, value, location):
        node = Node(value)
        if location==0:
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif location==1:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            temp = self.head
            index = 0
            while index<location-1:
                temp = temp.next
                index+=1
            node.prev = temp
            node.next = temp.next
            temp.next.prev = node
            temp.next = node

    def deleteList(self, location):
        if self.head==None:
            print("no list available")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index=0
                while index<location-1:
                    curNode = curNode.next
                    index+=1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode

    def deleteFullList(self):
        node = self.head
        while node.next!=None:
            node.prev=None
            node=node.next
        self.head=None
        self.tail=None
        print("all elements deleted")

    def displayList(self):
        if self.head==None:
            print("no elements")
            return
        node = self.head
        while node!= None:
            print(node.nodeValue)
            node = node.next

    def reverseDisplayList(self):
        node = self.tail
        while node != None:
            print(node.nodeValue)
            node = node.prev


doublyLL = DoublyLL()
doublyLL.createList(77)
doublyLL.insertElement(55,1)
doublyLL.insertElement(44,0)
doublyLL.insertElement(66,0)
doublyLL.insertElement(22,3)

doublyLL.displayList()
print("-----------")
doublyLL.deleteList(3)

doublyLL.displayList()
print("------------")
doublyLL.deleteFullList()
doublyLL.displayList()


