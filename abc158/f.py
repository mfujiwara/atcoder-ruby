import bisect
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
MOD=998244353
N=int(input())
xds=[]
for _ in range(N):
    x,d=map(int, input().split())
    xds.append((x,d))
xds.sort()
tree=SegmentTree([i for i in range(N)],max,-10)
for i in range(N-1,-1,-1):
    x,d=xds[i]
    j=bisect.bisect_left(xds,(x+d,0))
    index=tree.query(i,j)
    tree.update(i,index)
dp = [0]*(N+1)
dp[N] = 1
for i in range(N-1,-1,-1):
    dp[i]=dp[i+1]
    index=tree.query(i,i+1)
    dp[i]+=dp[index+1]
    dp[i]%=MOD
print(dp[0])
