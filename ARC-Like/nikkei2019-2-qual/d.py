import collections
class SegmentTree:
    def __init__(self, init_val, seg_func, ide_ele):
        size = len(init_val)
        self.seg_func = seg_func
        self.ide_ele = ide_ele
        self.n = 1 << (size - 1).bit_length()
        self.node = [ide_ele] * 2 * self.n
        for i in range(size):
            self.node[self.n + i - 1] = init_val[i]
        for i in range(self.n - 2, -1, -1):
            self.node[i] = self.seg_func(self.node[2 * i + 1], self.node[2 * i + 2])

    def update(self, index, val):
        i = index + self.n - 1
        self.node[i] = val
        while i > 0:
            i = int((i - 1)//2)
            l = self.node[2*i+1]
            r = self.node[2*i+2]
            self.node[i] =  self.seg_func(l, r)
  
    def query(self, left, right):
        ret=self.ide_ele
        left+=self.n-1
        right+=self.n-1
        while left<right:
            if left%2==0:
                ret = self.seg_func(ret, self.node[left])
                left+=1
            if right%2==0:
                right-=1
                ret = self.seg_func(ret, self.node[right])
            left=int(left//2)
            right=int(right//2)
        return ret
def seg_func(a,b):
    if a==-1:
        return b
    if b==-1:
        return a
    return min(a,b)
N,M=map(int, input().split())
edges=collections.defaultdict(list) # l to (r,c)
for i in range(M):
    l,r,c=map(int, input().split())
    edges[l-1].append((r-1,c))
costs=[-1]*N
costs[0]=0
tree=SegmentTree([-1]*N,seg_func,-1)
tree.update(0,0)
for r,c in edges[0]:
    tree.update(r,c,)
for i in range(1,N):
    tree.update(i-1,-1)
    costs[i]=tree.query(0,N)
    if costs[i]==-1:
        break
    for r,c in edges[i]:
        tree.update(r,seg_func(costs[i]+c,tree.query(r,r+1)))
print(costs[-1])
