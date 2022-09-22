INF=pow(10,20)
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
array=list(map(int, input().split()))
edges=[[] for _ in range(N)]
costs=[0]*N
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
    costs[u]+=array[v]
    costs[v]+=array[u]
tree=SegmentTree([(c,i) for i,c in enumerate(costs)],min,(INF,-1))
done=[False]*N
ret=0
for i in range(N):
    c,index=tree.query(0,N)
    done[index]=True
    tree.update(index,(INF,-1))
    ret=max(ret,c)
    for t in edges[index]:
        if done[t]: continue
        costs[t]-=array[index]
        tree.update(t,(costs[t],t))
print(ret)
