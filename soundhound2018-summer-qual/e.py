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
import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
union=UnionFind(N)
for _ in range(M):
    u,v,s=map(int, input().split())
    u-=1
    v-=1
    edges[u].append((v,s))
    edges[v].append((u,s))
    if len(edges[u])>1:
        union.unite(edges[u][-1][0],edges[u][-2][0])
    if len(edges[v])>1:
        union.unite(edges[v][-1][0],edges[v][-2][0])
if union.size()==1:
    values=[None]*N
    values[0]=1
    targets=[0]
    while targets:
        t=targets.pop()
        for u,s in edges[t]:
            if values[u]==None:
                values[u]=s-values[t]
                targets.append(u)
            else:
                if values[u]!=s-values[t]:
                    vt=values[t]
                    vu=values[u]
                    diff=s-vt-vu
                    if diff%2!=0:
                        print(0)
                        exit()
                    else:
                        values=[None]*N
                        values[t]=vt+diff//2
                        values[u]=vu+diff//2
                        targets=[]
                        break    
    for i in range(N):
        if values[i]!=None:
            targets.append(i)
    if len(targets)==N:
        print(1)
        exit()
    while targets:
        t=targets.pop()
        for u,s in edges[t]:
            if values[u]==None:
                values[u]=s-values[t]
                targets.append(u)
            else:
                if values[u]!=s-values[t]:
                    print(0)
                    exit()
    for v in values:
        if v<1:
            print(0)
            exit()
    print(1)
else:
    values=[None]*N
    min0=1
    min1=pow(10,10)
    targets=[0]
    values[0]=1
    while targets:
        t=targets.pop()
        for u,s in edges[t]:
            if values[u]==None:
                values[u]=s-values[t]
                if union.get_parent(u)==union.get_parent(0):
                    min0=min(min0,values[u])
                else:
                    min1=min(min1,values[u])
                targets.append(u)
            else:
                if values[u]!=s-values[t]:
                    print(0)
                    exit()
    ret=max(0,min0+min1-1)
    print(ret)
