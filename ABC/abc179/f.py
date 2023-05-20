N,Q=map(int, input().split())
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
ret=pow(N-2,2)
tree1=Bit(N)
tree1.add(1,N-2)
tree2=Bit(N)
tree2.add(1,N-2)
stop1=[N]
stop2=[N]
for _ in range(Q):
    t,x=map(int, input().split())
    if t==1:
        tree_x=tree1
        tree_y=tree2
        stop_x=stop1
        stop_y=stop2
    else:
        tree_x=tree2
        tree_y=tree1
        stop_x=stop2
        stop_y=stop1
    v=tree_x.sum(x)
    ret-=v
    if x<stop_x[0]:
        stop_x[0]=x
        # N-2 -> 1
        y=N-1-v
        w=tree_y.sum(1)
        # w->x-2
        tree_y.add(1,x-2-w)
        tree_y.add(stop_y[0], w-x+2)
print(ret)
