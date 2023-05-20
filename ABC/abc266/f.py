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
edge_list=[]
edges=[[] for _ in range(N)]
for _ in range(N):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
    edge_list.append((u,v))
path=[]
onpath=[False]*N
targets=[(0,0,-1)]
while targets:
    t,status,p=targets.pop()
    if status==0:
        targets.append((t,1,p))
        onpath[t]=True
        path.append(t)
        for u in edges[t]:
            if u==p: continue
            if onpath[u]:
                path.append(u)
                targets=[]
                break
            targets.append((u,0,t))
    else:
        onpath[t]=False
        path.pop()
#print(path)
loop_start=path.pop()
loop=set([loop_start])
while path[-1]!=loop_start:
    loop.add(path.pop())
#print(loop)
union=UnionFind(N)
for u,v in edge_list:
    if u in loop and v in loop:
        continue
    union.unite(u,v)
Q=int(input())
for _ in range(Q):
    x,y=map(int, input().split())
    x-=1
    y-=1
    if union.is_same_parent(x,y):
        print("Yes")
    else:
        print("No")
