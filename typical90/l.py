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
H,W=map(int, input().split())
MAP=[[False]*W for _ in range(H)]
Q=int(input())
union=UnionFind(H*W)
for _ in range(Q):
    q=list(map(int, input().split()))
    if q[0]==1:
        r,c=q[1]-1,q[2]-1
        MAP[r][c]=True
        n=r*W+c
        if r>0 and MAP[r-1][c]:
            union.unite(n,(r-1)*W+c)
        if r<H-1 and MAP[r+1][c]:
            union.unite(n,(r+1)*W+c)
        if c>0 and MAP[r][c-1]:
            union.unite(n,r*W+c-1)
        if c<W-1 and MAP[r][c+1]:
            union.unite(n,r*W+c+1)
    else:
        ra,ca,rb,cb=q[1]-1,q[2]-1,q[3]-1,q[4]-1
        n1=ra*W+ca
        n2=rb*W+cb
        if MAP[ra][ca] and MAP[rb][cb] and union.is_same_parent(n1,n2):
            print("Yes")
        else:
            print("No")
