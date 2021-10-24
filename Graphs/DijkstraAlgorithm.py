from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertex = set()
        self.edges = defaultdict(list)
        self.distance = {}

    def addNode(self,vertex):
        self.vertex.add(vertex)

    def addEdge(self,vertex, edge, distance):
        self.edges[vertex].append(edge)
        self.distance[(vertex,edge)] = distance

def dijkstra(graph, initial):
    visited = {initial:0}
    path = defaultdict(list)
    nodes = set(graph.vertex)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode==None:
                    minNode=node
                elif visited[node]<visited[minNode]:
                    minNode=node

        if minNode==None:
            break
        nodes.remove(minNode)

        currweight = visited[minNode]
        for edge in graph.edges[minNode]:
            weight = currweight + graph.distance[(minNode,edge)]
            if weight < currweight or edge not in visited:
                visited[edge]=weight
                path[edge]:minNode

    return visited, path

g = Graph()
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addNode("F")
g.addNode("G")
g.addEdge("A", "B", 2)
g.addEdge("A", "C", 5)
g.addEdge("B", "C", 6)
g.addEdge("B", "D", 1)
g.addEdge("B", "E", 3)
g.addEdge("C", "F", 8)
g.addEdge("D", "E", 4)
g.addEdge("E", "G", 9)
g.addEdge("F", "G", 7)
print(g.edges)

print(g.distance)
print(dijkstra(g,"A"))