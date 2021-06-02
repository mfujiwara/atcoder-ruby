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
def seg_func(l,r):
    lmin,lmax=l
    rmin,rmax=r
    return (min(lmin,rmin),max(lmax,rmax))
N,K=map(int, input().split())
array=list(map(int, input().split()))
if N==K:
    print(1)
    exit()
minmaxs=[(a,a) for a in array]
tree=SegmentTree(minmaxs,seg_func,(N,-1))
rets=[1]
for i in range(N-K):
    mini,maxi=tree.query(i,i+K+1)
    if array[i]==mini and array[i+K]==maxi:
        rets.append(False)
    else:
        rets.append(True)
rets2=[]
c=0
for i in range(K-2):
    if array[i]<array[i+1]:
        c+=1
    else:
        c=0
for i in range(K-2,N-1):
    if array[i]<array[i+1]:
        c+=1
    else:
        c=0
    if c>=K-1:
        rets2.append(False)
    else:
        rets2.append(True)
yet=True
ret=0
for i in range(N-K+1):
    if yet:
        if rets[i]:
            ret+=1
            if not rets2[i]:
                yet=False
    else:
        if rets[i] and rets2[i]:
            ret+=1
print(ret)