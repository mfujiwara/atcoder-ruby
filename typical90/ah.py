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
    return min(a,b)
N,K=map(int, input().split())
array=list(map(int, input().split()))
ret=0
r=0
INF=1<<60
lasts={}
tree=SegmentTree([(INF,0)]*N,seg_func,(INF,0))
for i,a in enumerate(array):
    if a in lasts:
        r+=1
        ret=max(ret,r)
        tree.update(lasts[a],(INF,0))
        lasts[a]=i
        tree.update(i,(i,a))
    elif len(lasts)<K:
        r+=1
        ret=max(ret,r)
        lasts[a]=i
        tree.update(i,(i,a))
    else:
        index,d=tree.query(0,N)
        lasts.pop(d)
        lasts[a]=i
        tree.update(index,(INF,0))
        tree.update(i,(i,a))
        r=i-index
print(ret)
