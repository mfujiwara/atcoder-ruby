import collections


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        i+=1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i+=1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
N,M,Q=map(int, input().split())
last_update=[-1]*N
memo=[(Q,-1)]
queies=[]
for i in range(Q):
    query=list(map(int, input().split()))
    queies.append(query)
    if query[0]==2:
        last_update[query[1]-1]=i
    elif query[0]==3:
        if last_update[query[1]-1]!=-1:
            memo.append((last_update[query[1]-1],query[2]-1))
memo.sort(reverse=True)
tree=Bit(M+1)
diffs=collections.defaultdict(int)
for index,query in enumerate(queies):
    #print([tree.sum(i) for i in range(M)],diffs)
    if query[0]==1:
        l,r,x=query[1:]
        l-=1
        tree.add(l,x)
        tree.add(r,-x)
    elif query[0]==2:
        i=query[1]-1
        x=query[2]
        while memo[-1][0]==index:
            _,j=memo.pop()
            diffs[(i,j)]=x-tree.sum(j)
    else:
        i,j=query[1:]
        i-=1
        j-=1
        print(tree.sum(j)+diffs[(i,j)])
