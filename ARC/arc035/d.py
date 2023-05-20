import math
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
logv=[0]
logsum=[0]
for i in range(1,pow(10,6)*2+1):
    v=math.log2(i)
    logsum.append(logsum[-1]+v)
N=int(input())
tree=Bit(N-1) # 0からiまでの経路数の対数
p,q=map(int, input().split())
vals=[0]*N
pq=[(p,q)]
def calc(p1,q1,p2,q2):
    x=abs(p1-p2)
    y=abs(q1-q2)
    return logsum[x+y]-logsum[x]-logsum[y]
for i in range(1,N):
    p,q=map(int, input().split())
    vals[i]=calc(p,q,pq[-1][0],pq[-1][1])
    tree.add(i,vals[i])
    pq.append((p,q))
Q=int(input())
for _ in range(Q):
    t=list(map(int, input().split()))
    if t[0]==1:
        k,a,b=t[1:]
        pq[k-1]=(a,b)
        if k>1:
            tree.add(k-1,-vals[k-1])
            vals[k-1]=calc(a,b,pq[k-2][0],pq[k-2][1])
            tree.add(k-1,vals[k-1])
        if k<N:
            tree.add(k,-vals[k])
            vals[k]=calc(a,b,pq[k][0],pq[k][1])
            tree.add(k,vals[k])
    else:
        l1,r1,l2,r2=t[1:]
        v1=tree.sum(r1-1)-tree.sum(l1-1)
        v2=tree.sum(r2-1)-tree.sum(l2-1)
        if v1>v2:
            print("FIRST")
        else:
            print("SECOND")
    #print([tree.sum(i)-tree.sum(i-1) for i in range(1,N)])
