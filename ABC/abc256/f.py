MOD=998244353
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
tree0=Bit(N)
tree1=Bit(N)
tree2=Bit(N)
for i in range(N):
    tree2.add(i+1,(i+1)*(i+1)*array[i])
    tree1.add(i+1,(i+1)*array[i])
    tree0.add(i+1,array[i])
for _ in range(Q):
    query=list(map(int, input().split()))
    if query[0]==1:
        i,v=query[1:]
        i-=1
        tree2.add(i+1,-(i+1)*(i+1)*array[i])
        tree1.add(i+1,-(i+1)*array[i])
        tree0.add(i+1,-array[i])
        array[i]=v
        tree2.add(i+1,(i+1)*(i+1)*array[i])
        tree1.add(i+1,(i+1)*array[i])
        tree0.add(i+1,array[i])
    else:
        i=query[1]
        i-=1
        val=tree2.sum(i+1)
        val-=(2*(i+1)+3)*tree1.sum(i+1)
        val+=(i+2)*(i+3)*tree0.sum(i+1)
        val//=2
        val%=MOD
        print(val)
