class UnionFind:
    def __init__(self, size):
        self.rank = [0]*size
        self.parent = [i for i in range(size)]
        self.counts = [1]*size

    def unite(self, id_x, id_y):
        x_parent = self.get_parent(id_x)
        y_parent = self.get_parent(id_y)
        if x_parent == y_parent:
            return 
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
            self.counts[x_parent] += self.counts[y_parent]
        else:
            self.parent[x_parent] = y_parent
            self.counts[y_parent] += self.counts[x_parent]
            if self.rank[x_parent] == self.rank[y_parent]:
                self.rank[y_parent] += 1 

    def get_parent(self, id_x):
        if self.parent[id_x] == id_x:
            return id_x
        else:
            self.parent[id_x] = self.get_parent(self.parent[id_x])
            return self.parent[id_x]

    def is_same_parent(self, id_x, id_y):
        return self.get_parent(id_x) == self.get_parent(id_y)

    def same_parent_conut(self, id_x):
        x_parent = self.get_parent(id_x)
        return self.counts[x_parent]

    def size(self):
        s=set()
        for x in self.parent:
            s.add(self.get_parent(x))
        return len(s)

N,M=map(int, input().split())
union=UnionFind(N)
ret=1
for _ in range(M):
    a,b=map(int, input().split())
    union.unite(a-1,b-1)
    ret=max(ret,union.same_parent_conut(a-1))
print(ret)
