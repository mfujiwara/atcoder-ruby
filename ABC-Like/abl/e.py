class LazySegmentTree:
    def __init__(self, init_val, seg_func, lazy_seg_func, update_func, ide_ele, lazy_ide_ele):
        size = len(init_val)
        self.seg_func = seg_func
        self.lazy_seg_func = lazy_seg_func
        self.update_func = update_func
        self.ide_ele = ide_ele
        self.lazy_ide_ele = lazy_ide_ele
        self.n = 1 << (size - 1).bit_length()
        self.node = [ide_ele] * 2 * self.n
        self.lazy = [lazy_ide_ele] * 2 * self.n
        for i in range(size):
            self.node[self.n + i - 1] = init_val[i]
        for i in range(self.n - 2, -1, -1):
            self.node[i] = self.seg_func(self.node[2 * i + 1], self.node[2 * i + 2])
        self.init_node = self.node[:]

    def update(self, a, b, x):
        stack=[]
        targets=[(0,0,self.n)]
        while targets:
            nexts=[]
            for k, l, r in targets:
                self.eval(k)
                if a <= l and r <= b:
                    self.lazy[k]=self.lazy_seg_func(self.lazy[k], x)
                    self.eval(k)
                elif a < r and l < b:
                    stack.append(k)
                    nexts.append((k*2+1,l,(l+r)//2))
                    nexts.append((k*2+2,(l+r)//2,r))
            targets = nexts
        while stack:
            k = stack.pop()
            l = self.node[2*k+1]
            r = self.node[2*k+2]
            self.node[k] =  self.seg_func(l, r)
        #print(f"self.node:{self.node}")
        #print(f"self.lazy_node:{self.lazy}")

    def query(self, left, right):
        left+=self.n-1
        right+=self.n-1
        # 遅延評価するために辿るノードを一旦保存
        stack=[]
        while left<right:
            if left%2==0:
                stack.append(left)
                left+=1
            if right%2==0:
                right-=1
                stack.append(right)
            left=int(left//2)
            right=int(right//2)
        # えばる
        ret=self.ide_ele
        while stack:
            k=stack.pop()
            self.eval(k)
            ret = self.seg_func(ret, self.node[k])
        return ret
    
    def eval(self, k):
        if self.lazy[k] != self.lazy_ide_ele:
            self.node[k] = self.update_func(self.init_node[k], self.lazy[k])

            if k < self.n - 1:
                self.lazy[2*k+1] = self.lazy_seg_func(self.lazy[2*k+1],self.lazy[k])
                self.lazy[2*k+2] = self.lazy_seg_func(self.lazy[2*k+2],self.lazy[k])
            
            self.lazy[k] = self.lazy_ide_ele
MOD=998244353
def seg_func(a,b):
    return (a+b)%MOD
def lazy_seg_func(a,b):
    return b
def update_func(a,b):
    return a*b%MOD
N,Q=map(int, input().split())
array=[pow(10,i,MOD)  for i in range(N)]
tree=LazySegmentTree(array,seg_func,lazy_seg_func,update_func,0,0)
for _ in range(Q):
    l,r,d=map(int, input().split())
    tree.update(N-r,N-l+1,d)
    v=tree.query(0,N)
    print(v)
