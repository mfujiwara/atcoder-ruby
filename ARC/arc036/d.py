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
N,Q=map(int, input().split())
union=UnionFind(2*N)
odds=[-1]*N
for _ in range(Q):
    w,x,y,z=map(int, input().split())
    x-=1
    y-=1
    if w==1:
        if z%2==0:
            union.unite(x,y)
            union.unite(x+N,y+N)
        else:
            union.unite(x,y+N)
            union.unite(x+N,y)
    else:
        if union.is_same_parent(x,y):
            print("YES")
        else:
            print("NO")
