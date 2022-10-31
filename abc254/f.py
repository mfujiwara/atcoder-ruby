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
                ret = self.seg_func(ret, self.node[left])
                left+=1
            if right%2==0:
                right-=1
                ret = self.seg_func(ret, self.node[right])
            left=int(left//2)
            right=int(right//2)
        return ret
N,Q=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_diff=[]
b_diff=[]
for i in range(N-1):
    a_diff.append(abs(a_array[i]-a_array[i+1]))
    b_diff.append(abs(b_array[i]-b_array[i+1]))
def seg_func(a,b):
    return math.gcd(a,b)
a_tree=SegmentTree(a_diff,seg_func,0)
b_tree=SegmentTree(b_diff,seg_func,0)
for _ in range(Q):
    h1,h2,w1,w2=map(int, input().split())
    ret=a_array[h1-1]+b_array[w1-1]
    if h1!=h2:
        ret=math.gcd(ret,a_tree.query(h1-1,h2-1))
    if w1!=w2:
        ret=math.gcd(ret,b_tree.query(w1-1,w2-1))
    print(ret)
