import QueuesUsingLinkedList as queue

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertElement(rootNode, value):
    if rootNode.data == None:
        rootNode.data = value
        return
    elif value<rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTreeNode(value)
        else:
            insertElement(rootNode.leftChild, value)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTreeNode(value)
        else:
            insertElement(rootNode.rightChild, value)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        q = queue.Queue()
        q.enqueue(rootNode)
        while not(q.isEmpty()):
            root = q.dequeue()
            print(root.data)

            if root.leftChild is not None:
                q.enqueue(root.leftChild)

            if root.rightChild is not None:
                q.enqueue(root.rightChild)
        return



def searchElement(rootNode, searchValue):
    if rootNode.data == searchValue:
        print("key found")
    elif searchValue < rootNode.data:
        if rootNode.leftChild.data == searchValue:
            print("key found")
        else:
            searchElement(rootNode.leftChild,searchValue)
    else:
        if rootNode.rightChild.data == searchValue:
            print("key found")
        else:
            searchElement(rootNode.rightChild,searchValue)

def getMinElement(rootNode):
    node = rootNode.leftChild
    while node.leftChild is not None:
        node = node.leftChild
    return node


def deleteNode(rootNode, value):
    if rootNode.data is None:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = getMinElement(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    return rootNode

def deleteBSTFullTree(rootNode):
    rootNode.rightChild = None
    rootNode.leftChild = None
    rootNode.data = None




bst = BinarySearchTreeNode(70)
insertElement(bst, 30)
insertElement(bst,100)
insertElement(bst,80)
print(bst.data)
print(bst.leftChild.data)
print(bst.rightChild.data)
print(bst.rightChild.leftChild.data)
searchElement(bst, 30)
print("------")
levelOrderTraversal(bst)
print("------")
deleteNode(bst,70)
levelOrderTraversal(bst)
print("------")
deleteBSTFullTree(bst)
levelOrderTraversal(bst)


