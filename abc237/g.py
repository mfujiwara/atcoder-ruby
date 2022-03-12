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

    def gindex(self, l, r):
        L = l + self.n
        R = r + self.n
        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1
        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1; R >>= 1
        while L:
            yield L
            L >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            if self.lazy[i-1] == self.lazy_ide_ele:
                continue
            self.lazy[2*i-1] = self.lazy_seg_func(self.lazy[2*i-1], self.lazy[i-1])
            self.lazy[2*i] = self.lazy_seg_func(self.lazy[2*i], self.lazy[i-1])
            self.node[2*i-1] = self.update_func(self.node[2*i-1], self.lazy[i-1])
            self.node[2*i] = self.update_func(self.node[2*i], self.lazy[i-1])
            self.lazy[i-1] = self.lazy_ide_ele

    def update(self, a, b, x):
        self.propagates(*self.gindex(a, b))
        L = self.n + a
        R = self.n + b
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = self.lazy_seg_func(self.lazy[R-1],x)
                self.node[R-1] = self.update_func(self.node[R-1],x)
            if L & 1:
                self.lazy[L-1] = self.lazy_seg_func(self.lazy[L-1], x)
                self.node[L-1] = self.update_func(self.node[L-1], x)
                L += 1
            L >>= 1; R >>= 1
        for i in self.gindex(a, b):
            v = self.seg_func(self.node[2*i-1], self.node[2*i])
            self.node[i-1] = self.update_func(v, self.lazy[i-1])

    def query(self, left, right):
        self.propagates(*self.gindex(left, right))
        L = self.n + left
        R = self.n + right

        s = self.ide_ele
        while L < R:
            if R & 1:
                R -= 1
                s = self.seg_func(s, self.node[R-1])
            if L & 1:
                s = self.seg_func(s, self.node[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s
N,Q,X=map(int, input().split())
array=list(map(int, input().split()))
array=[(1,0,0,1) if a<X else (0,1,0,1) if a==X else (0,0,1,1) for a in array]
index=array.index((0,1,0,1))
def seg_func(a,b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3])
def lazy_seg_func(a,b):
    return max(a,b)
def update_func(a,x):
    if x[1]==0:
        return a
    total=a[3]
    return [
        total if x[1]==1 else 0,
        total if x[1]==2 else 0,
        total if x[1]==3 else 0,
        total
    ]
tree=LazySegmentTree(array,seg_func,lazy_seg_func,update_func,(0,0,0,0),(0,0))
for q in range(Q):
    c,l,r=map(int, input().split())
    l-=1
    t1,t2,t3,total=tree.query(l,r)
    if c==1:
        if t1>0:
            tree.update(l,l+t1,(q+1,1))
        if t2>0:
            tree.update(l+t1,l+t1+t2,(q+1,2))
            index=l+t1
        if t3>0:
            tree.update(l+t1+t2,l+t1+t2+t3,(q+1,3))
    else:
        if t3>0:
            tree.update(l,l+t3,(q+1,3))
        if t2>0:
            tree.update(l+t3,l+t3+t2,(q+1,2))
            index=l+t3
        if t1>0:
            tree.update(l+t3+t2,l+t3+t2+t1,(q+1,1))
print(index+1)
