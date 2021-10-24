from collections import defaultdict

class tpsort:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,vertex, edge):
        self.graph[vertex].append(edge)

    #this method starts from start node i.e. node with 0 in-degree, here for loop takes vertices with 0 in-degree
    def topologicalSort(self,vertex):
        visited=[]
        stack=[]
        for v in list(self.graph):
            if v not in visited:
                self.tsort(v, visited, stack)

        print(stack)

    # this method starts from start vertex i.e. node with 0 in-degree and goes till last vertex
    def tsort(self, vtx, visited, stack):
        visited.append(vtx)
        for i in self.graph[vtx]:
            if i not in visited:
                self.tsort(i, visited, stack)
        stack.insert(0,vtx)




g = tpsort()
g.addEdge('A','C')
g.addEdge('B','C')
g.addEdge('B','D')
g.addEdge('C','E')
g.addEdge('D','F')
g.addEdge('E','H')
g.addEdge('E','F')
g.addEdge('F','G')

print(g.graph)
g.topologicalSort('A')
