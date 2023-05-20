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
MOD=998244353
N,M=map(int, input().split())
edges=collections.defaultdict(set)
union=UnionFind(N)
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].add(v)
    edges[v].add(u)
    union.unite(u,v)
if N!=M:
    print(0)
    exit()
one=[]
for i in range(N):
    if len(edges[i])==0:
        print(0)
        exit()
    elif len(edges[i])==1:
        one.append(i)
while one:
    t=one.pop()
    u=list(edges[t])[0]
    edges[t]=set()
    edges[u].remove(t)
    if len(edges[u])==0:
        print(0)
        exit()
    elif len(edges[u])==1:
        one.append(u)
for i in range(N):
    if len(edges[i])==0: continue
    if len(edges[i])>2:
        print(0)
        exit()
print(pow(2,union.size(),MOD))
