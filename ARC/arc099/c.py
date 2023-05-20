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
ab=[[0]*N for _ in range(N)]
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    ab[a][b]=1
    ab[b][a]=1
targets=[True]*N
counts=[1]*N
while True:
    change=False
    for i in range(N):
        if not targets[i]: continue
        group=[]
        for j in range(N):
            if not targets[j] or i==j or ab[i][j]==1:
                continue
            group.append(j)
        if len(group)>1:
            change=True
            k1=group.pop()
            for k2 in group:
                if ab[k1][k2]==0:
                    print(-1)
                    exit()
                for j in range(N):
                    ab[k1][j]=ab[k1][j]&ab[k2][j]
                    ab[j][k1]=ab[k1][j]
                targets[k2]=False
                counts[k1]+=counts[k2]
    if not change:
        break
#print(targets)
pairs=[]
for i in range(N):
    if not targets[i]: continue
    for j in range(N):
        if not targets[j]or i==j: continue
        if ab[i][j]==0:
            pairs.append((counts[i],counts[j]))
            targets[i]=False
            targets[j]=False
            break
    if targets[i]:
        pairs.append((counts[i],0))
        targets[i]=False
#print(pairs)
dp=set([0])
for i,j in pairs:
    nexts=set()
    for c in dp:
        nexts.add(c+i)
        nexts.add(c+j)
    dp=nexts
mini=N
for d in dp:
    mini=min(mini,abs(N-2*d))
r1=(N-mini)//2
r2=r1+mini
ret=r1*(r1-1)//2+r2*(r2-1)//2
print(ret)
