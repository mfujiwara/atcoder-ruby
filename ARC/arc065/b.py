import collections
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

    def is_same_parent(self, id_x, id_y):
        return self.get_parent(id_x) == self.get_parent(id_y)

    def size(self):
        s=set()
        for x in self.parent:
            s.add(self.get_parent(x))
        return len(s)
N,K,L=map(int, input().split())
union1=UnionFind(N)
for _ in range(K):
    p,q=map(int, input().split())
    union1.unite(p-1,q-1)
union2=UnionFind(N)
for _ in range(L):
    r,s=map(int, input().split())
    union2.unite(r-1,s-1)
counts=collections.defaultdict(int)
for i in range(N):
    counts[(union1.get_parent(i),union2.get_parent(i))]+=1
print(*[counts[(union1.get_parent(i),union2.get_parent(i))] for i in range(N)])
