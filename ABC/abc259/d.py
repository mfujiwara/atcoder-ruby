class UnionFind:
    def __init__(self, size):
        self.rank = [0]*size
        self.parent = [i for i in range(size)]
        # self.counts = [1]*size

    def unite(self, id_x, id_y):
        x_parent = self.get_parent(id_x)
        y_parent = self.get_parent(id_y)
        if x_parent == y_parent:
            return 
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
            # self.counts[x_parent] += self.counts[y_parent]
        else:
            self.parent[x_parent] = y_parent
            # self.counts[y_parent] += self.counts[x_parent]
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

    # def same_parent_conut(self, id_x):
    #     x_parent = self.get_parent(id_x)
    #     return self.counts[x_parent]

    def size(self):
        s=set()
        for x in self.parent:
            s.add(self.get_parent(x))
        return len(s)
N=int(input())
sx,sy,tx,ty=map(int, input().split())
sss=[]
ttt=[]
xyr=[]
for i in range(N):
    x,y,r=map(int, input().split())
    xyr.append((x,y,r))
    if pow(x-sx,2)+pow(y-sy,2)==pow(r,2):
        sss.append(i)
    if pow(x-tx,2)+pow(y-ty,2)==pow(r,2):
        ttt.append(i)
union=UnionFind(N)
for i in range(N-1):
    ix,iy,ir=xyr[i]
    for j in range(i+1,N):
        jx,jy,jr=xyr[j]
        if ix==jx and iy==jy:
            if ir==jr:
                union.unite(i,j)
        elif pow(ix-jx,2)+pow(iy-jy,2)<=pow(ir+jr,2):
            union.unite(i,j)
#print(sss,ttt)
for s in sss:
    for t in ttt:
        if union.is_same_parent(s,t):
            print("Yes")
            exit()
print("No")
