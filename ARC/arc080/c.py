import heapq
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
array=list(map(int, input().split()))
INF=N+1
even=[(INF,-1)]*N
odd=[(INF,-1)]*N
for i,a in enumerate(array):
    if i%2==0:
        even[i]=(a,i)
    else:
        odd[i]=(a,i)
tree_even=SegmentTree(even,min,(INF,-1))
tree_odd=SegmentTree(odd,min,(INF,-1))
# queue:=区間の最小値,min index, max indexの3つ組
queue=[(tree_even.query(0,N),0,N)]
rets=[]
for _ in range(N//2):
    #print(queue)
    (s,s_index),l,r=heapq.heappop(queue)
    if s_index%2==0:
        t,t_index=tree_odd.query(s_index+1,r)
    else:
        t,t_index=tree_even.query(s_index+1,r)
    rets.append(s)
    rets.append(t)
    for start,end in [(l,s_index),(s_index+1,t_index),(t_index+1,r)]:
        if start!=end:
            if start%2==0:
                mini=tree_even.query(start,end)
            else:
                mini=tree_odd.query(start,end)
            heapq.heappush(queue,(mini,start,end))
print(*rets)
