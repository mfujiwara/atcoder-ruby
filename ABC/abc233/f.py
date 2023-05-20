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
N=int(input())
array=list(map(int, input().split()))
M=int(input())
union=UnionFind(N)
edges_to_i={}
counts=[0]*N
edges=collections.defaultdict(list)
for i in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges_to_i[(a,b)]=i+1
    if not union.is_same_parent(a,b):
        union.unite(a,b)
        edges[a].append(b)
        edges[b].append(a)
        counts[a]+=1
        counts[b]+=1
for i,a in enumerate(array):
    if not union.is_same_parent(i,a-1):
        print(-1)
        exit()
targets=[]
for i,c in enumerate(counts):
    if c==1:
        targets.append(i)
rets=[]
while targets:
    t=targets.pop()
    def search(route):
        last=route[-1]
        if array[last]==t+1:
            return route
        for u in edges[last]:
            if u not in route:
                route.append(u)
                v=search(route)
                if v!=-1:
                    return route
                else:
                    route.pop()
        return -1
    rrr=search([t])
    for i in range(len(rrr)-2,-1,-1):
        a=rrr[i]
        b=rrr[i+1]
        if a>b:
            a,b=b,a
        rets.append(edges_to_i[(a,b)])
        array[a],array[b]=array[b],array[a]
    for u in edges[t]:
        edges[u].remove(t)
        if len(edges[u])==1:
            targets.append(u)
print(len(rets))
print(*rets)
