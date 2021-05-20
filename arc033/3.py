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
Q=int(input())
tree=Bit(200002)
array=[]
for _ in range(Q):
    t,x=map(int, input().split())
    if t==1:
        tree.add(x,1)
    else:
        left=0
        right=200000
        while True:
            if left+1==right:
                print(right)
                tree.add(right,-1)
                break
            mid=(left+right)//2
            if tree.sum(mid)<x:
                left=mid
            else:
                right=mid
