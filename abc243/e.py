import collections
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
N,M=map(int, input().split())
abc=[]
edges=collections.defaultdict(list)
for _ in range(M):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    abc.append((a,b,(c,-1)))
    edges[a].append((b,(c,-1)))
    edges[b].append((a,(c,-1)))
distances=[]
size=N
INF=pow(10,12)
for i in range(N):
    start=i
    done=[False]*size
    shortest=[(INF,0)]*size
    shortest[start]=(0,0)
    pred={}
    queue=[((0,0), start)]
    heapq.heapify(queue)

    while len(queue)>0:
        cost, u = heapq.heappop(queue)
        if shortest[u]<cost: continue
        done[u] = True    #探されたuは確定

        for v,cc in edges[u]:
            if done[v]: continue
            aa = (shortest[u][0] + cc[0],shortest[u][1] + cc[1])
            if aa < shortest[v]:
                shortest[v]=aa
                heapq.heappush(queue, (aa,v))
                pred[v] = u
    distances.append(shortest)
abc.sort(key=lambda e:e[2])
union=UnionFind(N)
ret=0
edges=collections.defaultdict(list)
for a,b,c in abc:
    if not union.is_same_parent(a,b):
        union.unite(a,b)
        edges[a].append((b,c))
        edges[b].append((a,c))
    elif distances[a][b]<c:
        ret+=1
print(ret)
