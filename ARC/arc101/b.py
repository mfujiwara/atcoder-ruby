import itertools
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
M=(N+1)*N//2
array=list(map(int, input().split()))
left=1
right=max(array)+1
while left+1!=right:
    mid=(left+right)//2
    tmp=[1 if a>=mid else -1 for a in array]
    sums=list(itertools.accumulate(tmp))
    mini=min(min(sums),0) # 1
    maxi=max(sums) # maxi-mini+1
    diff=1-mini
    tree=Bit(maxi+diff)
    tree.add(diff,1)
    count=0
    for s in sums:
        s+=diff
        count+=tree.sum(s)
        tree.add(s,1)
    if count>=(M+1)//2:
        left=mid
    else:
        right=mid
print(left)
