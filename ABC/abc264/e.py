class UnionFind:
    def __init__(self, size1,size2):
        self.rank = [0]*(size1+size2)
        self.parent = [i for i in range(size1+size2)]
        self.counts1 = [1]*size1+[0]*size2 # 都市の数
        self.counts2 = [0]*size1+[1]*size2 # 発電支所の数

    def unite(self, id_x, id_y):
        x_parent = self.get_parent(id_x)
        y_parent = self.get_parent(id_y)
        if x_parent == y_parent:
            return 0
        if self.counts2[x_parent]==0 and self.counts2[y_parent]!=0:
            ret=self.counts1[x_parent]
        elif self.counts2[x_parent]!=0 and self.counts2[y_parent]==0:
            ret=self.counts1[y_parent]
        else:
            ret=0
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
            self.counts1[x_parent] += self.counts1[y_parent]
            self.counts2[x_parent] += self.counts2[y_parent]
        else:
            self.parent[x_parent] = y_parent
            self.counts1[y_parent] += self.counts1[x_parent]
            self.counts2[y_parent] += self.counts2[x_parent]
            if self.rank[x_parent] == self.rank[y_parent]:
                self.rank[y_parent] += 1 
        return ret

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
N,M,E=map(int, input().split())
edges=[]
for _ in range(E):
    u,v=map(int, input().split())
    edges.append((u-1,v-1))
Q=int(input())
queries=[]
for _ in range(Q):
    x=int(input())
    queries.append(x-1)
query_set=set(queries)
union=UnionFind(N,M)
ret=0
for i,(u,v) in enumerate(edges):
    if i not in query_set:
        ret+=union.unite(u,v)
rets=[ret]
while queries:
    x=queries.pop()
    u,v=edges[x]
    ret+=union.unite(u,v)
    rets.append(ret)
rets.pop()
while rets:
    print(rets.pop())
