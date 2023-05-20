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
N,Q=map(int, input().split())
array=list(map(int, input().split()))
array=[0]+array
q_dic=defaultdict(list)
for i in range(Q):
    l,r=map(int, input().split())
    q_dic[r].append((i,l,r))
most_rights=[-1]*(N+1)
tree=Bit(N)
rets=[-1]*Q
for i in range(1,N+1):
    a=array[i]
    if most_rights[a]!=-1:
        tree.add(most_rights[a],-1)
    most_rights[a]=i
    tree.add(i,1)
    for k,l,r in q_dic[i]:
        r=tree.sum(r)-tree.sum(l-1)
        rets[k]=r
for r in rets:
    print(r)
