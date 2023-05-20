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
H,W,h1,w1,h2,w2=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(H)]
h2=min(h1,h2)
w2=min(w1,w2)
if h1==h2 and w1==w2:
    print(0)
    exit()
sums=[[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        v=A[i][j]
        if i>0:
            v+=sums[i-1][j]
        if j>0:
            v+=sums[i][j-1]
        if i>0 and j>0:
            v-=sums[i-1][j-1]
        sums[i][j]=v
t_scores=[[0]*(W-w1+1) for _ in range(H-h1+1)]
for i in range(H-h1+1):
    for j in range(W-w1+1):
        v=sums[i+h1-1][j+w1-1]
        if i>0:
            v-=sums[i-1][j+w1-1]
        if j>0:
            v-=sums[i+h1-1][j-1]
        if i>0 and j>0:
            v+=sums[i-1][j-1]
        t_scores[i][j]=v
a_scores=[[0]*(W-w2+1) for _ in range(H-h1+1)]
for j in range(W-w2+1):
    init_val=[]
    for i in range(H-h2+1):
        v=sums[i+h2-1][j+w2-1]
        if i>0:
            v-=sums[i-1][j+w2-1]
        if j>0:
            v-=sums[i+h2-1][j-1]
        if i>0 and j>0:
            v+=sums[i-1][j-1]
        init_val.append(v)
    tree=SegmentTree(init_val,max,0)
    for i in range(H-h1+1):
        a_scores[i][j]=tree.query(i,i+h1-h2+1)
a_trees=[]
for scores in a_scores:
    a_trees.append(SegmentTree(scores,max,0))
ret=0
for i in range(H-h1+1):
    for j in range(W-w1+1):
        t=t_scores[i][j]
        a=a_trees[i].query(j,j+w1-w2+1)
        ret=max(ret,t-a)
print(ret)
