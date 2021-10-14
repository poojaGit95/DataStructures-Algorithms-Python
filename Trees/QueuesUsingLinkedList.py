class Node:
    def __init__(self,value):
        self.nodeValue = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node


    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        else:
            delnode = self.linkedList.head.nodeValue
            self.linkedList.head = self.linkedList.head.next
            return delnode

    def display(self):
        if self.isEmpty():
            print("empty queue")
            return
        else:
            node = self.linkedList.head
            while node is not None:
                print(node.nodeValue)
                node = node.next


    def peek(self):
        if self.isEmpty():
            print("empty queue")
            return
        else:
            return self.linkedList.head.nodeValue


    def deleteQueue(self):
        if self.isEmpty():
            print("no queue")
            return
        else:
            self.linkedList.head = None
            self.linkedList.tail = None


