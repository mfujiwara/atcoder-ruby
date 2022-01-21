import heapq
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
N,M,Q=map(int, input().split())
cabs=[]
for _ in range(M):
    a,b,c=map(int, input().split())
    heapq.heappush(cabs,(c,a-1,b-1,-1))
for i in range(Q):
    u,v,w=map(int, input().split())
    heapq.heappush(cabs,(w,u-1,v-1,i))
rets=["No"]*Q
union=UnionFind(N)
count=0
while cabs:
    c,a,b,i=heapq.heappop(cabs)
    if union.is_same_parent(a,b): continue
    if i>=0:
        rets[i]="Yes"
    else:
        union.unite(a,b)
        count+=1
        if count==N-1:
            break
for ret in rets:
    print(ret)
