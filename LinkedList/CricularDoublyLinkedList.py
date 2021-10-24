class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.nodeValue = value

class CircularDLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def createList(self,value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    def displayElements(self):
        node = self.head
        if node == None:
            print("no values")
            return
        while node:
            print(node.nodeValue)
            if(node.next==self.head):
                break
            node = node.next

    def insertElements(self,value,location):
        node = Node(value)
        if location==0:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.tail.next = self.head
        elif location==1:
            node.next = self.head
            node.prev = self.tail
            self.tail.next = node
            self.tail=node
        else:
            temp = self.head
            index=0
            while index<location-1:
                temp = temp.next
                index+=1
            temp.next.prev = node
            node.next = temp.next
            temp.next = node
            node.prev=temp

    def deleteElements(self,location):
        if self.head==None:
            print ("No elements present")
        else:
            if location==0:
                if(self.head==self.tail):
                    self.head.next=None
                    self.head.prev=None
                    self.head=None
                    self.tail=None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next=self.head
            elif location==1:
                if (self.head == self.tail):
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev=self.tail
            else:
                temp = self.head
                index=0
                while index<location-1:
                    temp=temp.next
                    index+=1
                temp.next = temp.next.next
                temp.next.prev = temp

    def deleteList(self):
        node = self.head
        while node.next!=self.head:
            node.prev = None
            node=node.next
        self.head=None
        self.tail=None
        print("all elements deleted")

    def reverseDisplayList(self):
        node = self.tail
        while node:
            print(node.nodeValue)
            if(node.prev == self.tail):
                break
            node = node.prev

circulardll = CircularDLL()
circulardll.createList(11)
circulardll.insertElements(22,0)
circulardll.insertElements(44,0)
circulardll.insertElements(33,1)
circulardll.insertElements(55,2)
circulardll.displayElements()
print("---------")
circulardll.deleteList()


circulardll.displayElements()


