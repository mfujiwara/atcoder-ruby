from collections import defaultdict
INF=-10**7
class SegmentTree:
    def __init__(self, source):
        self.n=1
        while self.n < len(source):
            self.n = self.n*2
        self.node=[INF]*2*self.n
        for index,val in enumerate(source):
            i = index + self.n - 1
            self.node[i]=val
        for i in range(self.n-2,-1,-1):
            l = self.node[2*i+1]
            r = self.node[2*i+2]
            self.node[i] = l if l > r else r

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

N,M=map(int, input().split())
array=list(map(int, input().split()))
seg=SegmentTree([-i for i in range(2*10**6)])
counts=defaultdict(int)
for i in range(M):
    a=array[i]
    counts[a]+=1
    if counts[a]==1:
        seg.update(a,INF)
ret=abs(seg.get_max())
for i in range(N-M):
    a=array[M+i]
    counts[a]+=1
    if counts[a]==1:
        seg.update(a,INF)
    b=array[i]
    counts[b]-=1
    if counts[b]==0:
        seg.update(b,-b)
    ret=min(ret,abs(seg.get_max()))
print(ret)
