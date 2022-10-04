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
abct=[]
ng=pow(10,6)
ok=0
for _ in range(M):
    a,b,c,t=map(int, input().split())
    abct.append((a,b,c,t))
    ng=min(ng,c/t)
    ok=max(ok,c/t)
while ng+0.001<ok:
    #print("lr",ng,ok)
    # mid以下にできるか
    mid=(ng+ok)/2
    total_c=0
    total_t=0
    union=UnionFind(N)
    abct2=[]
    for a,b,c,t in abct:
        v=c-mid*t
        abct2.append((v,a,b,c,t))
    abct2.sort(reverse=True)
    while abct2:
        v,a,b,c,t=abct2.pop()
        if not union.is_same_parent(a,b) or v<=0:
            union.unite(a,b)
            total_c+=c
            total_t+=t
    #print(total_c/total_t,mid)
    if total_c/total_t<=mid:
        ok=mid
    else:
        ng=mid
print(ok)
