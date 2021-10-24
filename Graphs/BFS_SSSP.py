class Graph:
    def __init__(self, gdict):
        if gdict is None:
            gdict= {}
        self.gdict = gdict

    def traversal(self, vertex):
        visited = {}
        parent = {}
        queue = []
        path = []

        for v in list(self.gdict):
            visited[v] = False
            parent[v] = None

        path.append(vertex)
        visited[vertex] = True
        queue.append(vertex)
        while queue:
            deq = queue.pop(0)
            for adj in self.gdict[deq]:
                if not(visited[adj]):
                    queue.append(adj)
                    parent[adj] = deq
        return path

    def bfs_path(self,start,end):
        path = []
        v = end
        while v!=start:
            path.append(v)
           # v = parent[v]
        print(reversed(path))

    def bfs(self,start,end):
        queue = []
        queue.append(start)
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return  path

            for adj in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)


dict = {"a":["b","c"], "b":["d","g"], "c":["d", "e"], "d":["f"], "e":["f"], "g":["f"]}
dict2 = {"a":["b","c"], "b":["a","d","g"], "c":["a", "d", "e"], "d":["b","c","f"], "e":["c","f"], "f": ["d", "e"], "g":["b","f"]}
new_dict = {}
g = Graph(dict)
g2 = Graph(dict2)
g1 = Graph(new_dict) #2.1 BFS: Breadth First Search Implementation in Python | Graph Data Structure --> Pytech vision
#print(g.gdict)
#print(g.bfs("a","f"))
#print(g.traversal("a"))
print(g.bfs("a","d"))