INF=pow(10,9)
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
array=[]
for i in range(N):
    l,r=map(int, input().split())
    array.append((l,r,i,i))
def seg_func(a,b):
    al,ar,ai,aj=a
    bl,br,bi,bj=b
    if al>=bl:
        cl,ci=al,ai
    else:
        cl,ci=bl,bi
    if ar<br:
        cr,cj=ar,aj
    else:
        cr,cj=br,bj
    return (cl,cr,ci,cj)
tree=SegmentTree(array,seg_func,(0,INF,-1,-1))
mini=-INF
maxi=INF
base=0
ret=0
while True:
    l,r,i,j=tree.query(0,N)
    #print("query",l,r,i,j)
    tree.update(i,(0,INF,-1,-1))
    tree.update(j,(0,INF,-1,-1))
    maxi=max(min(l,maxi),mini)
    mini=min(max(r,mini),maxi)
    if i==-1:
        break
    if i==j:
        ret+=base
        #print(maxi)
    else:
        diff=maxi-mini
        ret+=base*2+diff
        base+=diff
        #print(maxi,mini)
print(ret)
