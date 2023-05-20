N=int(input())
# edges[x]:座標xにある辺の(開始位置,終了位置,領域に入る出る)を表す3つ組
edges=[[] for _ in range(pow(10,5)+1)]
for _ in range(N):
    M=int(input())
    MOD=2*M
    array=list(map(int, input().split()))
    xyy=[]
    for i in range(M):
        basei=i*2
        x1=array[basei]
        y1=array[basei+1]
        x2=array[(basei+2)%MOD]
        y2=array[(basei+3)%MOD]
        if x1==x2:
            xyy.append((x1,y1,y2))
    xyy.sort()
    _,y1,y2=xyy[0]
    d=1 if y1<y2 else -1
    for x,y1,y2 in xyy:
        if y1<y2:
            edges[x].append((y1,y2,d))
        else:
            edges[x].append((y2,y1,-d))
#print(edges[:13])
query=[[] for _ in range(pow(10,5))]
Q=int(input())
for i in range(Q):
    x,y=map(int, input().split())
    query[x].append((y,i))
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
rets=[0]*Q
tree=Bit(pow(10,5)+1)
for x in range(pow(10,5)):
    for y1,y2,v in edges[x]:
        tree.add(y1,v)
        tree.add(y2,-v)
    # print([tree.sum(y) for y in range(8)])
    # if x>13: break
    for y,i in query[x]:
        rets[i]=tree.sum(y)
print(*rets,sep="\n")
