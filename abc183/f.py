from collections import defaultdict
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
N,Q=map(int, input().split())
array=list(map(int, input().split()))
union=UnionFind(N)
classes=[defaultdict(int) for i in range(N)]
for i in range(N):
    classes[i][array[i]-1]+=1
for _ in range(Q):
    q,a,b=map(int, input().split())
    if q==1:
        pa=union.get_parent(a-1)
        pb=union.get_parent(b-1)
        if pa==pb: continue
        if len(classes[pa])>len(classes[pb]):
            merged=classes[pa]
            for key in classes[pb]:
                merged[key]+=classes[pb][key]
        else:
            merged=classes[pb]
            for key in classes[pa]:
                merged[key]+=classes[pa][key]
        union.unite(a-1, b-1)
        p=union.get_parent(a-1)
        classes[p]=merged
    else:
        pa=union.get_parent(a-1)
        print(classes[pa][b-1])
