class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

def makeConnected(n, connections):
    uf = UnionFind(n)
    extra_connections = 0
    
    for u, v in connections:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
        else:
            extra_connections += 1
    
    components = len(set(uf.find(i) for i in range(n)))
    
    if extra_connections >= components - 1:
        return components - 1
    else:
        return -1

# Input
n = int(input())  # Number of available cities
m = int(input())  # Number of routes
connections = []
for _ in range(m):
    u, v = map(int, input().split())
    connections.append([u, v])

result = makeConnected(n, connections)
print(result)
