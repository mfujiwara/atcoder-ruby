import sys
class UnionFind:
    def __init__(self, size):
        self.rank = [0]*size
        self.parent = [i for i in range(size)]

    def unite(self, id_x, id_y):
        x_parent = self.get_parent(id_x)
        y_parent = self.get_parent(id_y)
        if x_parent == y_parent:
            return 
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[x_parent] = y_parent
            if self.rank[x_parent] == self.rank[y_parent]:
                self.rank[y_parent] += 1 

    def get_parent(self, id_x):
        if self.parent[id_x] == id_x:
            return id_x
        else:
            self.parent[id_x] = self.get_parent(self.parent[id_x])
            return self.parent[id_x]

    def size(self, n):
        s=set()
        for i in range(N):
            s.add(self.get_parent(self.parent[i]))
        return len(s)


N,M=map(int, input().split())
union=UnionFind(N+M)
for i in range(N):
    array=list(map(int, input().split()))
    array=array[1:]
    for l in array:
        union.unite(i,N+l-1)
if union.size(N)==1:
    print("YES")
else:
    print("NO")
