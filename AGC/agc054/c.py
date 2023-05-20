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
MOD=998244353
N,K=map(int, input().split())
array=list(map(int, input().split()))
tree=Bit(N)
ret=1
for a in array:
    potential=N-a
    count=tree.sum(N)-tree.sum(a)
    #print(f"{potential} {count}")
    if count==K and potential-count>0:
        ret*=(potential-count+1)
        ret%=MOD
    tree.add(a,1)
print(ret)
