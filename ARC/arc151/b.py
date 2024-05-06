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
array=list(map(int, input().split()))
for i in range(N):
    array[i]-=1
ret=0
nokori=N
t=M*(M-1)//2%MOD
union=UnionFind(N)
for i in range(N):
    j=array[i]
    if not union.is_same_parent(i,j):
        v=pow(M,nokori-2,MOD)
        ret+=v*t%MOD
        ret%=MOD
        nokori-=1
        union.unite(i,j)
print(ret)
