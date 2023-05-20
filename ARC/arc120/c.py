from collections import defaultdict
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
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
diffs=defaultdict(list)
for i,a in enumerate(a_array):
    diffs[a+i].append(i)
perm=[-1]*N
idxs=defaultdict(int)
for i,b in enumerate(b_array):
    bi=b+i
    if len(diffs[bi])<=idxs[bi]:
        print(-1)
        exit()
    j=diffs[bi][idxs[bi]]
    idxs[bi]+=1
    perm[i]=j
tree=Bit(N)
ret=0
for i,j in enumerate(perm):
    k=j+tree.sum(j+1)
    ret+=k-i
    tree.add(1,1)
    tree.add(j+1,-1)
print(ret)
