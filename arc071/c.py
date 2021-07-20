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
def seg_func(a,b):
    return a+b
S=input()
T=input()
ss=[]
for ch in S:
    if ch=="A":
        ss.append(1)
    else:
        ss.append(-1)
tt=[]
for ch in T:
    if ch=="A":
        tt.append(1)
    else:
        tt.append(-1)
s_tree=SegmentTree(ss,seg_func,0)
t_tree=SegmentTree(tt,seg_func,0)
q=int(input())
for _ in range(q):
    a,b,c,d=map(int, input().split())
    v=s_tree.query(a-1,b)
    w=t_tree.query(c-1,d)
    if v%3==w%3:
        print("YES")
    else:
        print("NO")
