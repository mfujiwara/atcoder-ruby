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
N=int(input())
xy=[]
xxx=set()
yyy=set()
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
    xxx.add(x)
    yyy.add(y)
xxx=sorted(list(xxx))
yyy=sorted(list(yyy))
X_to_x={}
for i,x in enumerate(xxx):
    X_to_x[x]=i+1
Y_to_y={}
for i,y in enumerate(yyy):
    Y_to_y[y]=i+1
counts=[[0]*4 for _ in range(N)]
xyi=[]
for i in range(N):
    x,y=xy[i]
    xyi.append((X_to_x[x],Y_to_y[y],i))
xyi.sort()
tree2=Bit(len(yyy))
tree1=Bit(len(yyy))
for x,y,i in xyi:
    counts[i][2]=tree2.sum(y)
    tree2.add(y,1)
    counts[i][1]=tree1.sum(len(yyy)-y+1)
    tree1.add(len(yyy)-y+1,1)
tree0=Bit(len(yyy))
tree3=Bit(len(yyy))
for x,y,i in xyi[::-1]:
    counts[i][0]=tree0.sum(len(yyy)-y+1)
    tree0.add(len(yyy)-y+1,1)
    counts[i][3]=tree3.sum(y)
    tree3.add(y,1)
ret=0
pow2=[1]
for _ in range(N):
    pow2.append(pow2[-1]*2%MOD)
#print(counts)
for ccc in counts:
    for i in range(4):
        ccc[i]=pow2[ccc[i]]-1
    # oooo
    ret+=ccc[0]*ccc[1]%MOD*ccc[2]%MOD*ccc[3]%MOD*2%MOD
    ret%=MOD
    # ooox
    ret+=ccc[0]*ccc[1]%MOD*ccc[2]%MOD*2%MOD
    ret%=MOD
    # ooxo
    ret+=ccc[0]*ccc[1]%MOD*ccc[3]%MOD*2%MOD
    ret%=MOD
    # ooxx
    ret+=ccc[0]*ccc[1]%MOD
    ret%=MOD
    # oxoo
    ret+=ccc[0]*ccc[2]%MOD*ccc[3]%MOD*2%MOD
    ret%=MOD
    # oxox
    ret+=ccc[0]*ccc[2]%MOD*2%MOD
    ret%=MOD
    # oxxo
    ret+=ccc[0]*ccc[3]%MOD
    ret%=MOD
    # oxxx
    ret+=ccc[0]
    ret%=MOD
    # xooo
    ret+=ccc[1]*ccc[2]%MOD*ccc[3]%MOD*2%MOD
    ret%=MOD
    # xoox
    ret+=ccc[1]*ccc[2]%MOD
    ret%=MOD
    # xoxo
    ret+=ccc[1]*ccc[3]%MOD*2%MOD
    ret%=MOD
    # xoxx
    ret+=ccc[1]
    ret%=MOD
    # xxoo
    ret+=ccc[2]*ccc[3]%MOD
    ret%=MOD
    # xxox
    ret+=ccc[2]
    ret%=MOD
    # xxxo
    ret+=ccc[3]
    ret%=MOD
    # xxxx
    ret+=1
    ret%=MOD
    #print(ccc,ret)
print(ret)
#print(counts)

