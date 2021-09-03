import collections
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
H,W,M=map(int, input().split())
mini_x=[H]*W
all_y=[[W] for _ in range(H)]
for _ in range(M):
    x,y=map(int, input().split())
    all_y[x-1].append(y-1)
    mini_x[y-1]=min(mini_x[y-1],x-1)
ret=0
for v in mini_x:
    if v==0: break
    ret+=v
tree=Bit(W)
done=[False]*W
for x in range(H):
    if x==0:
        for yy in range(min(all_y[0]),W):
            if yy==W: continue
            done[yy]=True
            tree.add(yy,1)
        continue
    min_y=min(all_y[x])
    if min_y==0:
        break
    ret+=tree.sum(min_y-1)
    for yy in all_y[x]:
        if yy==W: continue
        if done[yy]: continue
        done[yy]=True
        tree.add(yy,1)
print(ret)
