class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.nodes = []
        self.graph = []

    def addNode(self, node):
        self.nodes.append(node)

    def add_edge(self, src, dest, dist):
        self.graph.append([src, dest, dist])

    def distanceFromSource(self, dist):
        for node, wgt in dist.items():
            print("Distance of vertex", node, "is", wgt)

    def BellmanFord(self, src):
        dist = {}
        for i in self.nodes:
            dist[i] = float("inf")
        dist[src] = 0

        for i in range(1, self.vertices):
            for s,d,w in self.graph:
                if dist[s]!=float("inf") and dist[d]>dist[s]+w:
                    dist[d] = dist[s]+w

        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[d] > dist[s] + w:
                print("graph has negative cycle")
                return

        self.distanceFromSource(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.BellmanFord("E")
