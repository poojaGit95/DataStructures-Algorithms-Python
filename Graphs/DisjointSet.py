class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in self.vertices:
            self.parent[v]=v
        self.rank = dict.fromkeys(self.vertices, 0)

    def find(self, element):
        if self.parent[element] == element:
            return element
        else:
            return self.find(self.parent[element])

    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot]<self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot]>self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot]+=1

v = ["A", "B", "C", "D", "E"]
disjointset = DisjointSet(v)
disjointset.union("A", "B")
disjointset.union("C", "B")
print(disjointset.find("C"))


