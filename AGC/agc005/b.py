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

# 遅延評価セグメント木
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
            self.node[k] = self.update_func(self.node[k], self.lazy[k])
            if k < self.n - 1:
                self.lazy[2*k+1] = self.lazy_seg_func(self.lazy[2*k+1],self.lazy[k])
                self.lazy[2*k+2] = self.lazy_seg_func(self.lazy[2*k+2],self.lazy[k])
            self.lazy[k] = self.ide_ele
N=int(input())
array=list(map(int, input().split()))
array=[(i,a) for i,a in enumerate(array)]
def seg_func(a,b):
    if a[1]<b[1]:
        return a
    else:
        return b
tree=SegmentTree(array,seg_func,(-1,2*pow(10,5)))
targets=[(0,N)]
ret=0
while targets:
    t=targets.pop()
    if t[0]==t[1]-1:
        ret+=array[t[0]][1]
        continue
    i,v=tree.query(t[0],t[1])
    if i==t[0]:
        ret+=v*(t[1]-t[0])
        targets.append((i+1,t[1]))
    elif i==t[1]-1:
        ret+=v*(t[1]-t[0])
        targets.append((t[0],i))
    else:
        ret+=v*(i-t[0]+1)*(t[1]-i)
        targets.append((t[0],i))
        targets.append((i+1,t[1]))
print(ret)
