class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        """i=0には足せない"""
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
N=int(input())
array=list(map(int, input().split()))
a_tree=Bit(N+1)
b_tree=Bit(N+1)
for i in range(1,N+1):
    a_tree.add(i,1)
    b_tree.add(i,-1)
for i in range(1,N):
    p1=array[i-1]
    p2=array[i]
    v1=a_tree.sum(p1)+b_tree.sum(p1)
    v2=a_tree.sum(p2)+b_tree.sum(p2)
    if v1+1==v2:
        continue
    diff=v1+1-v2
    if diff>0:
        a_tree.add(p2,diff)
        if p2<N:
            b_tree.add(p2+1,-diff)
    else:
        b_tree.add(p2,diff)
        if p2<N:
            a_tree.add(p2+1.-diff)
b_tree.add(1,1-b_tree.sum(N))
a_ret=[]
b_ret=[]
for i in range(1,N+1):
    a_ret.append(str(a_tree.sum(i)))
    b_ret.append(str(b_tree.sum(i)))
print(" ".join(a_ret))
print(" ".join(b_ret))
