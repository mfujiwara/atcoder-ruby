import heapq
INF=-10**10
class SegmentTree:
    def __init__(self, size):
        self.n=1
        while self.n < size:
            self.n = self.n*2
        self.node=[INF]*2*self.n
  
    def update(self, index, val):
        i = index + self.n - 1
        self.node[i] = val
        while i > 0:
            i = int((i - 1)//2)
            l = self.node[2*i+1]
            r = self.node[2*i+2]
            self.node[i] =  l if l > r else r
  
    def get_max(self):
        return self.node[0]
N,Q=map(int, input().split())
ab=[list(map(int, input().split())) for _ in range(N)]
arrays=[[] for _ in range(200000)]
for i in range(N):
    a,b=ab[i]
    arrays[b-1].append((-a,i))
tree=SegmentTree(200000)
for i,array in enumerate(arrays):
    heapq.heapify(array)
    if array:
        r,index=array[0]
        tree.update(i,r)
for _ in range(Q):
    c,d=map(int, input().split())
    a,b=ab[c-1]
    ab[c-1]=a,d
    heapq.heappush(arrays[d-1],(-a,c-1))
    tree.update(d-1,arrays[d-1][0][0])
    while arrays[b-1]:
        _,i=heapq.heappop(arrays[b-1])
        aa,bb=ab[i]
        if bb==b:
            heapq.heappush(arrays[b-1], (-aa,i))
            tree.update(bb-1,-aa)
            break
    if not arrays[b-1]:
        tree.update(b-1,INF)
    print(abs(tree.get_max()))
