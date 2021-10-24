class Node:
    def __init__(self, value=None):
        self.nodeValue = value
        self.nodeNext = None


class singlyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates linked list with 1 element
    def createList(self):
        node = Node('Pooja')
        self.head = node
        self.tail = node

    # inserts element into linked list based on location given
    def insertElement(self, element, location):
        node = Node(element)
        # when list is empty
        if self.head is None:
            self.head = node
            self.tail = node
        # when list is non empty
        else:
            if location == 0:               # when list is non empty and inserting element at first
                node.nodeNext = self.head
                self.head = node
            elif location == 1:              # when list is non empty and inserting element at last
                self.tail.nodeNext = node
                self.tail = node
            else:                            # when list is non empty and inserting element in middle
                index = 0
                tempnode = self.head
                while index < location-1:
                    tempnode = tempnode.nodeNext
                    index+=1
                temp = tempnode.nodeNext
                tempnode.nodeNext = node
                node.nodeNext = temp

    # removes element from the linked list based on the position or element value given
    def deleteElement(self, value):
        node = self.head
        prev = self.head
        if node is None:
            print("List empty")
        else:
            if value is not None:
                while self.head is not None:
                    if(node.nodeValue == value):
                        temp = node.nodeNext
                        prev.nodeNext = temp
                        break
                    prev = node
                    node = node.nodeNext


    # searches linked list if element is present
    def searchElement(self, value):
        node = self.head
        while node is not None:
            if value == node.nodeValue:
                return ("element present")
            node = node.nodeNext
        return ("element not in list")


    # prints all elements of linked list
    def display(self):
        node = self.head
        if(node is None):
            print("No linked list elements")
            return
        while node is not None:
            print(node.nodeValue)
            node = node.nodeNext


s = singlyLinkedList()
s.createList()
s.insertElement('raghav',1)
s.insertElement('rani',1)
s.insertElement('raja',1)
s.insertElement('rajesh',2)
print(s.searchElement("Pooja"))
s.deleteElement("raghav")
s.deleteElement("rani")
s.display()
