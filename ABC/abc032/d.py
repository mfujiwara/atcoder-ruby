#knapsack
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
N,W=map(int, input().split())
max_v=0
max_w=0
vws=[]
for _ in range(N):
    v,w=map(int, input().split())
    vws.append((v,w))
    max_v=max(max_v,v)
    max_w=max(max_w,w)
if N==1:
    v,w=vws[0]
    if w<=W:
        print(v)
    else:
        print(0)
elif N<=30:
    def calc(vws):
        rets=[]
        for i in range(2**len(vws)):
            k=0
            v_sum=0
            w_sum=0
            while i>0:
                i,r=divmod(i,2)
                if r==1:
                    v,w=vws[k]
                    v_sum+=v
                    w_sum+=w
                k+=1
            if w_sum<=W:
                rets.append((w_sum,v_sum))
        return rets
    vws1=vws[:N//2]
    vws2=vws[N//2:]
    wvs1=calc(vws1)
    wvs2=calc(vws2)
    wvs1.sort()
    wvs2.sort()
    ret=0
    def seg_func(a,b):
        return (max(a[0],b[0]),max(a[1],b[1]))
    tree=SegmentTree(wvs2,seg_func,(0,0))
    for w,v in wvs1:
        i=bisect.bisect_left(wvs2,(W-w+1,0))
        if i==0:
            v2=0
        else:
            _,v2=tree.query(0,i)
        ret=max(ret,v+v2)
    print(ret)
elif max_w<=1000:
    L=1000*200
    dp=[-1]*(L+1)
    dp[0]=0
    ret=0
    for v,w in vws:
        for i in range(L,-1,-1):
            if dp[i]==-1: continue
            nw=w+i
            if nw>W: continue
            dp[nw]=max(dp[nw],dp[i]+v)
            ret=max(ret,dp[nw])
    print(ret)
else:
    L=1000*200
    dp=[-1]*(L+1)
    dp[0]=0
    ret=0
    for v,w in vws:
        for i in range(L,-1,-1):
            if dp[i]==-1: continue
            nw=w+dp[i]
            nv=v+i
            if nw>W: continue
            if dp[nv]==-1:
                dp[nv]=nw
            else:
                dp[nv]=min(dp[nv],nw)
            ret=max(ret,nv)
    print(ret)
