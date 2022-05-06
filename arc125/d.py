import collections
MOD=998244353
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
N=int(input())
array=[0]+list(map(int, input().split()))
last_index=collections.defaultdict(int)
tree=Bit(N)
for i in range(1,N+1):
    a=array[i]
    if last_index[a]==0:
        last_index[a]=i
        v=tree.sum(i)+1
        tree.add(i,v)
    else:
        v=tree.sum(i)-tree.sum(last_index[a]-1)
        tree.add(i,v)
        tree.add(last_index[a],tree.sum(last_index[a]-1)-tree.sum(last_index[a]))
        last_index[a]=i
    #print(*[tree.sum(i) for i in range(1,N+1)])
print(tree.sum(N))
