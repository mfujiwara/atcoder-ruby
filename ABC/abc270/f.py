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
N,M=map(int, input().split())
x_array=list(map(int, input().split()))
y_array=list(map(int, input().split()))
edges=[]
for _ in range(M):
    a,b,z=map(int, input().split())
    a-=1
    b-=1
    edges.append((z,a,b))
# 空海なし
edges.sort()
union=UnionFind(N)
ret0=0
count=N-1
for i,(z,a,b) in enumerate(edges):
    if not union.is_same_parent(a,b):
        union.unite(a,b)
        ret0+=z
        count-=1
        if count==0:
            edges=edges[:i+1]
            break
if union.size()>1:
    ret0=pow(10,20)
edges2=edges.copy()
# 空だけ
for i in range(N):
    edges.append((x_array[i],i,N))
edges.sort()
union=UnionFind(N+1)
ret1=0
count=N
for i,(z,a,b) in enumerate(edges):
    if not union.is_same_parent(a,b):
        union.unite(a,b)
        ret1+=z
        count-=1
        if count==0:
            edges=edges[:i+1]
            break
if union.size()>1:
    ret1=pow(10,20)
# 空海あり
for i in range(N):
    edges.append((y_array[i],i,N+1))
edges.sort()
union=UnionFind(N+2)
ret2=0
count=N+1
for z,a,b in edges:
    if not union.is_same_parent(a,b):
        union.unite(a,b)
        ret2+=z
        count-=1
        if count==0:
            break
if union.size()>1:
    ret2=pow(10,20)
# 海だけ
for i in range(N):
    edges2.append((y_array[i],i,N))
edges2.sort()
union=UnionFind(N+1)
ret3=0
count=N
for z,a,b in edges2:
    if not union.is_same_parent(a,b):
        union.unite(a,b)
        ret3+=z
        count-=1
        if count==0:
            break
if union.size()>1:
    ret3=pow(10,20)
print(min(ret0,ret1,ret2,ret3))
