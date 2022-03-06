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
            i += i & -i
N=int(input())
lr=(-2000,1)
tree=Bit(1)
tree.add(1,1)
for _ in range(N):
    p,l=map(int, input().split())
    nexts=Bit(2*l+1)
    for i in range(1,2*l+2):
        if p-l-1+i>lr[0]+lr[1]-1:
            nexts.add(i,tree.sum(lr[1]))
            #print(tree.sum(lr[1]),end=" ")
        elif p-l-1+i<=lr[0]:
            #print(0,end=" ")
            continue
        else:
            # lr[0]+1->1
            # p-l-1+i->p-l-1+i-lr[0]
            #print(tree.sum(p-l-1+i-lr[0]),end=" ")
            nexts.add(i,tree.sum(p-l-1+i-lr[0]))
    #print()
    tree=nexts
    lr=(p-l,2*l+1)
print(tree.sum(lr[1]))
