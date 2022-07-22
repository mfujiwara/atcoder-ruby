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
N,M=map(int,input().split())
x_array=list(map(int,input().split()))
edges=collections.defaultdict(list)
yab=[]
for i in range(M):
  a,b,y=map(int,input().split())
  a-=1
  b-=1
  edges[a].append((b,y,i))
  edges[b].append((a,y,i))
  yab.append((y,a,b))
 
union=UnionFind(N)
yab.sort()
ok=[]
 
for y,a,b in yab:
    pa=union.get_parent(a)
    pb=union.get_parent(b)
    if not union.is_same_parent(pa,pb):
        union.unite(pa,pb)
        p=union.get_parent(pa)
        # 重みを親側に寄せる
        if p==pa:
            x_array[pa]+=x_array[pb]
            x_array[pb]=0
        else:
            x_array[pb]+=x_array[pa]
            x_array[pa]=0
    else:
        p=union.get_parent(pa)
    #print(x_array)
    if x_array[p]>=y:
        # 条件を満たすものを記録
        ok.append((y,a,b))
done=[False]*N
remain_set=set()
while ok:
    y,a,b=ok.pop()
    targets=[a,b]
    while targets:
        t=targets.pop()
        if done[t]: continue
        done[t]=True
        for u,c,i in edges[t]:
            if c<=y:
                # 基準になる辺の重さ以下の辺は条件を満たす
                remain_set.add(i)
                targets.append(u)
print(M-len(remain_set))
