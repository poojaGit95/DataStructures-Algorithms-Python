class Graphs:
    def __init__(self, gdict):
        if gdict is None:
            self.gdict = {}
        else:
            self.gdict = gdict

    def addEdge(self,vertex, edge):
        self.gdict[vertex].append(edge)

    def bfsTraversal(self,vertex):
        visited = []
        queue = [vertex]
        while len(queue) != 0:
            dequeue = queue.pop(0)
            if dequeue not in visited:
                print(dequeue)
                visited.append(dequeue)

            for adjVertex in self.gdict[dequeue]:
                if adjVertex not in visited:
                    queue.append(adjVertex)


    def dfsTraversal(self,vertex):
        visited = []
        stack = [vertex]
        while len(stack)!=0:
            popVertex = stack.pop()
            if popVertex not in visited:
                print(popVertex)
                visited.append(popVertex)

            for adjVertex in self.gdict[popVertex]:
                if adjVertex not in visited:
                    stack.append(adjVertex)

g = {'a':['b','c','d'], 'b':['a','e'], 'c':['a','d'], 'd':['c','e'], 'e':['b','d']}

graph = Graphs(g)
print(graph.gdict)
graph.addEdge('d','a')
print(graph.gdict['d'])
print("----------")
graph.bfsTraversal('a')
print("----------")
graph.dfsTraversal('a')