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
N,Q=map(int, input().split())
S=input()
sss=[]
sums=[0]
for ch in S:
    if ch=="(":
        sss.append(1)
        sums.append(sums[-1]+1)
    else:
        sss.append(-1)
        sums.append(sums[-1]-1)
def seg_func(a,b):
    return min(a,b)
def lazy_seg_func(a,b):
    return a+b
def update_func(a,b):
    return a+b
tree=LazySegmentTree(sums,seg_func,lazy_seg_func,update_func,pow(10,6),0)
#print("tree",*[tree.query(i,i+1) for i in range(N+1)])
for _ in range(Q):
    t,l,r=map(int, input().split())
    if t==1:
        if sss[l-1]!=sss[r-1]:
            x=2 if sss[l-1]==-1 else -2
            tree.update(l,r,x)
            sss[l-1],sss[r-1]=sss[r-1],sss[l-1]
            #print("tree",*[tree.query(i,i+1) for i in range(N+1)])
    else:
        s=tree.query(l-1,l)
        t=tree.query(r,r+1)
        #print("s,t",s,t)
        if s!=t:
            print("No")
            continue
        mini=tree.query(l,r+1)
        if mini<t:
            print("No")
        else:
            print("Yes")
