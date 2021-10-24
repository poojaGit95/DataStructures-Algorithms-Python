class Node:
    def __init__(self, value):
        self.nodeValue = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head== None:
            return True
        else:
            return False

    # inserting element at first place since time complexity is o(1)
    def push(self, value):
        node = Node(value)
        if self.isEmpty():  # inserting 1st element i.e. creating linked list
            self.LinkedList.head = node
        else:
            node.next = self.LinkedList.head
            self.LinkedList.head = node

    # deleting element at first place since time complexity is o(1)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            popnode = self.LinkedList.head
            self.LinkedList.head = self.LinkedList.head.next
            return popnode, "is poped"


    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.LinkedList.head.nodeValue

    def deleteStack(self):
        if self.isEmpty():
            return "Stack doesnt exist"
        else:
            self.LinkedList.head = None


    def display(self):
        if self.isEmpty():
            print("Stack empty")
            return
        else:
            node = self.LinkedList.head
            while node is not None:
                print(node.nodeValue)
                node = node.next



slist = Stack()
print(slist.isEmpty())
slist.display()
slist.push(11)
slist.push(12)
slist.push(13)
slist.display()
print("--------")
slist.pop()
print(slist.peek())
print("------")
slist.display()
print("------")
slist.deleteStack()
slist.display()
