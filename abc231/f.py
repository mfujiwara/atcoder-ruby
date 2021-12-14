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
N=int(input())
a_array=list(map(int, input().split()))
a_zip=sorted(list(set(a_array)))
a2zip={}
for i,a in enumerate(a_zip):
    a2zip[a]=i
b_array=list(map(int, input().split()))
b_zip=sorted(list(set(b_array)))
b2zip={}
for i,b in enumerate(b_zip):
    b2zip[b]=i
ab_array=[]
for i in range(N):
    a=a_array[i]
    b=b_array[i]
    ab_array.append((a2zip[a],b2zip[b]))
ab_array.sort()
def seg_func(a,b):
    return a+b
tree=SegmentTree([0]*len(b_zip),seg_func,0)
counts=[0]*len(b_zip)
i=N-1
ret=0
while i>=0:
    a=ab_array[i][0]
    bs=[]
    while i>=0 and ab_array[i][0]==a:
        b=ab_array[i][1]
        counts[b]+=1
        tree.update(b,counts[b])
        bs.append(b)
        i-=1
    for b in bs:
        ret+=tree.query(0,b+1)
print(ret)
