import QueuesUsingLinkedList as queue

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.leftChild = None
        self.rightChild = None


tree = TreeNode("Drinks")
leftChild = TreeNode("hot")
rightChild = TreeNode("cold")
tree.leftChild = leftChild
tree.rightChild = rightChild
leftChild.leftChild = TreeNode("tea")
leftChild.rightChild = TreeNode("coffee")
rightChild.leftChild = TreeNode("cola")
#rightChild.rightChild = TreeNode("fanta")


def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

# queues implemented using python list
def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
#    else:
#        qlist = queue.Queue()
#        qlist.enqueue(rootNode)
#       while not(qlist.isEmpty()):
#            node = qlist.dequeue()
#           print(node.data)

#            if(node.leftChild is not None):
#                qlist.enqueue(node.leftChild)

#            if (node.rightChild is not None):
#               qlist.enqueue(node.rightChild)

# queues implemented using linked list (import queue accordingly)
def levelOrderTraversalLinkedList(rootNode):
    if rootNode is None:
        return
    else:
        qlist = queue.Queue()
        qlist.enqueue(rootNode)
        while not(qlist.isEmpty()):
            node = qlist.dequeue()
            print(node.data)

            if(node.leftChild is not None):
                qlist.enqueue(node.leftChild)

            if (node.rightChild is not None):
                qlist.enqueue(node.rightChild)


def searchNode(rootNode, searchnode):
    if rootNode is None:
        return
    else:
        qlist = queue.Queue()
        qlist.enqueue(rootNode)
        while not(qlist.isEmpty()):
            root = qlist.dequeue()
            if(root.data == searchnode):
                return "element found"

            if (root.leftChild is not None):
                qlist.enqueue(root.leftChild)

            if (root.rightChild is not None):
                qlist.enqueue(root.rightChild)

        return "element not found"

def insertElement(rootnode, newnode):
    if rootnode is None:
        rootnode = newnode
        return
    else:
        qlist = queue.Queue()
        qlist.enqueue(rootnode)
        while not(qlist.isEmpty()):
            root = qlist.dequeue()
            if root.leftChild is not None:
                qlist.enqueue(root.leftChild)
            else:
                root.leftChild = newnode
                return "inserted successfully"

            if root.rightChild is not None:
                qlist.enqueue(root.rightChild)
            else:
                root.rightChild = newnode
                return "inserted successfully"

def getDeepestNode(rootNode):
    if rootNode is None:
        return
    else:
        qlist = queue.Queue()
        qlist.enqueue(rootNode)
        while not(qlist.isEmpty()):
            root = qlist.dequeue()

            if(root.leftChild is not None):
                qlist.enqueue(root.leftChild)

            if(root.rightChild is not None):
                qlist.enqueue(root.rightChild)

        deepestNode = root
        return  deepestNode

def deleteDeepestNode(rootNode, dnode):
    if rootNode is None:
        return
    else:
        qlist = queue.Queue()
        qlist.enqueue(rootNode)
        while not(qlist.isEmpty()):
            root = qlist.dequeue()
            if(root == dnode):
                root = None
                return

            if (root.leftChild is not None):
                if(root.leftChild == dnode):
                    root.leftChild = None
                    return
                else:
                    qlist.enqueue(root.leftChild)

            if (root.rightChild is not None):
                if (root.rightChild == dnode):
                    root.rightChild = None
                    return
                else:
                    qlist.enqueue(root.rightChild)


def deleteTreeNode(rootNode, node):
    if rootNode is None:
        return
    else:
        qlist = queue.Queue()
        qlist.enqueue(rootNode)
        while not(qlist.isEmpty()):
            root = qlist.dequeue()
            if root.data == node:
                dnode = getDeepestNode(rootNode)
                root.data = dnode.data
                deleteDeepestNode(rootNode,dnode)
                return

            if (root.leftChild is not None):
                qlist.enqueue(root.leftChild)

            if (root.rightChild is not None):
                qlist.enqueue(root.rightChild)


def deleteTree(rootNode):
    if rootNode is None:
        return "no tree"
    else:
        rootNode.rightChild=None
        rootNode.leftChild=None
        rootNode.data = None









#print("----PREORDER TRAVERSAL")
#preOrderTraversal(tree)
#print("----INORDER TRAVERSAL")
#inOrderTraversal(tree)
#print("----POSTORDER TRAVERSAL")
#postOrderTraversal(tree)
#print("----LEVEL ORDER TRAVERSAL")
#levelOrderTraversalLinkedList(tree)
#print("----SEARCH ELEMENT----")
#print(searchNode(tree,"cola"))
#print("----INSERT ELEMENT IN TREE----")
#newnode = TreeNode("fanta")
#insertElement(tree, newnode)
#levelOrderTraversalLinkedList(tree)
#print("----DELETE ELEMENT IN TREE----")
deleteTreeNode(tree,"cola")
#levelOrderTraversalLinkedList(tree)
#print("---DELETE FULL TREE---")
#deleteTree(tree)
levelOrderTraversalLinkedList(tree)





