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
N,M=map(int, input().split())
a_array=set()
b_array=set()
ab=[]
for _ in range(M):
    a,b=map(int, input().split())
    a_array.add(a)
    b_array.add(b)
    ab.append((a,b))
a_array=sorted(list(a_array))
b_array=sorted(list(b_array))
a2i={}
b2i={}
for i,a in enumerate(a_array):
    a2i[a]=i
for i,b in enumerate(b_array):
    b2i[b]=i
import collections
abab=collections.defaultdict(list)
for a,b in ab:
    a=a2i[a]
    b=b2i[b]
    abab[a].append(b)
def seg_func(a,b):
    return max(a,b)
tree=SegmentTree([0]*len(b_array),seg_func, 0)
ret=0
keys=sorted(list(abab.keys()))
for a in keys:
    updates={}
    for b in abab[a]:
        if b==0:
            v=1
        else:
            v=tree.query(0,b)+1
        updates[b]=v
    for b in updates:
        v=updates[b]
        ret=max(ret,v)
        tree.update(b,v)
print(ret)
