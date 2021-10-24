class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
INF = 9999
class FloydWarshall:

    def __init__(self):
        pass

    def printSolution(self, nodes, distanceMatrix):
        for i in range(nodes):
            for j in range(nodes):
                if distanceMatrix[i][j]!=INF:
                    print(distanceMatrix[i][j], end=" ")
                else:
                    print("INF", end=" ")
            print(" ")

    def shortestPathCal(self, nodes, graphMatrix):
        gMatrix = graphMatrix

        for k in range(nodes):
            for i in range(nodes):
                for j in range(nodes):
                    gMatrix[i][j] = min(graphMatrix[i][j], graphMatrix[i][k]+graphMatrix[k][j])

        self.printSolution(nodes, gMatrix)


g = Graph(3)
f = FloydWarshall()
m = [[1, 2, INF], [INF, 1, 1], [INF,2,4]]
f.printSolution(g.nodes, m)
print("================")
f.shortestPathCal(g.nodes, m)

