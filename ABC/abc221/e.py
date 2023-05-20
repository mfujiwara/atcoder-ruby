MOD=998244353
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            s%=MOD
            i -= i & -i
        return s

    def add(self, i, x):
        """i=0には足せない"""
        while i <= self.size:
            self.tree[i] += x
            self.tree[i]%=MOD
            i += i & -i
N=int(input())
array=list(map(int, input().split()))
pows=[1]
inv2=(MOD+1)//2
for _ in range(N):
    pows.append(pows[-1]*inv2%MOD)
a2i={}
for i,a in enumerate(sorted(set(array))):
    a2i[a]=i
for i in range(N):
    array[i]=a2i[array[i]]
array_with_index=[(a,i) for i,a in enumerate(array)]
array_with_index.sort()
tree=Bit(N)
memo=[-1]*N
for a,i in array_with_index:
    memo[i]=tree.sum(i+1)
    tree.add(i+1,pows[i+1])
ret=0
base=1
for i in range(N):
    ret+=memo[i]*base%MOD
    ret%=MOD
    base*=2
    base%=MOD
print(ret)
