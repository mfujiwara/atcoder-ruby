MOD=pow(10,9)+7
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            s %= MOD
            i -= i & -i
        return s

    def add(self, i, x):
        """i=0には足せない"""
        while i <= self.size:
            self.tree[i] += x
            self.tree[i] %= MOD
            i += i & -i
N,M=map(int, input().split())
pre={}
limits=[N]*N
fs=[]
for i in range(N):
    f=int(input())
    fs.append(f)
    if f in pre:
        limits[pre[f]]=i
    pre[f]=i
maxi=limits[-1]
for i in range(N-2,-1,-1):
    limits[i]=min(limits[i],limits[i+1])    
tree=Bit(N+1)
tree.add(1,1)
tree.add(limits[0]+1,-1)
for i in range(1,N):
    base=tree.sum(i)
    tree.add(i+1,base)
    tree.add(limits[i]+1,-base)    
print(tree.sum(N))
