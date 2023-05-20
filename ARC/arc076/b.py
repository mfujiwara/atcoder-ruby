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
xyi=[]
yxi=[]
for i in range(N):
    x,y=map(int, input().split())
    xyi.append((x,y,i))
    yxi.append((y,x,i))
xyi=sorted(xyi)
yxi=sorted(yxi)
edges=[]
for i in range(N-1):
    x1,_,i1=xyi[i]
    x2,_,i2=xyi[i+1]
    edges.append((abs(x1-x2),i1,i2))
for i in range(N-1):
    y1,_,i1=yxi[i]
    y2,_,i2=yxi[i+1]
    edges.append((abs(y1-y2),i1,i2))
edges=sorted(edges)
ret=0
count=0
union=UnionFind(N)
for c,i,j in edges:
    if not union.is_same_parent(i,j):
        union.unite(i,j)
        ret+=c
        count+=1
        if count==N-1:
            break
print(ret)
