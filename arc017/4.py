import math
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
                if ret==0:
                    ret = self.node[left]
                else:
                    ret = self.seg_func(ret, self.node[left])
                left+=1
            if right%2==0:
                right-=1
                if ret==0:
                    ret = self.node[right]
                else:
                    ret = self.seg_func(ret, self.node[right])
            left=int(left//2)
            right=int(right//2)
        return ret
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
N=int(input())
array=list(map(int, input().split()))
vals=[(a,1) for a in array] # value and count
diffs=[array[i] - array[i-1] if i>0 else array[0] for i in range(N)]
diffTree=SegmentTree(diffs,math.gcd,0)
def seg_func(a,b):
    return (a[0]+b[0],a[1]+b[1])
def lazy_seg_func(a,b):
    return a+b
def update_func(a,b):
    return (a[0]+b*a[1],a[1])
tree=LazySegmentTree(vals,seg_func,lazy_seg_func,update_func,(0,0),0)
M=int(input())
for _ in range(M):
    t,l,r=map(int, input().split())
    if t==0:
        v,_=tree.query(l-1,l)
        if l==r:
            print(v)
        else:
            d=diffTree.query(l,r)
            print(math.gcd(v,d))
    else:
        array[l-1]+=t
        diffs[l-1]+=t
        diffTree.update(l-1,diffs[l-1])
        if r<N:
            diffs[r]-=t
            diffTree.update(r,diffs[r])
        tree.update(l-1,r,t)
    # print([tree.query(i,i+1) for i in range(N)])
    # print([diffTree.query(i,i+1) for i in range(N)])

