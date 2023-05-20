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
N=int(input())
xy=[]
for i in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
union=UnionFind(N)
for i in range(N-1):
    xi,yi=xy[i]
    for j in range(i+1,N):
        xj,yj=xy[j]
        if xi-1==xj and yi-1==yj:
            union.unite(i,j)
        elif xi-1==xj and yi==yj:
            union.unite(i,j)
        elif xi==xj and yi-1==yj:
            union.unite(i,j)
        elif xi==xj and yi+1==yj:
            union.unite(i,j)
        elif xi+1==xj and yi==yj:
            union.unite(i,j)
        elif xi+1==xj and yi+1==yj:
            union.unite(i,j)
print(union.size())
#print(union.parent)
