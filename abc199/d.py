from collections import defaultdict
N,M=map(int, input().split())
edges=defaultdict(list)
for _ in range(M):
    a,b=map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
orders=[]
targets=[N-1-i for i in range(N)]
while len(orders)<N:
    t=targets.pop()
    if not t in orders:
        orders.append(t)
        targets += edges[t]
def check(colors,ord,orders,rate):
    ret=0
    if ord==N:
        return rate
    idx=orders[ord]
    neib=set()
    exist=False # 未確定の隣人がいる
    exist2=False # 確定済の隣人がいる
    for i in edges[idx]:
        if colors[i]!=-1:
            neib.add(colors[i])
            exist2=True
        else:
            exist=True
    if len(neib)==3:
        return 0
    if not exist2:
        colors[idx]=0
        ret+=check(colors,ord+1,orders,rate*3)
        colors[idx]=-1
    elif not exist:
        r=3-len(neib)
        ret+=check(colors,ord+1,orders,rate*r)
    else:
        for i in range(3):
            if not i in neib:
                colors[idx]=i
                ret+=check(colors,ord+1,orders,rate)
        colors[idx]=-1
    return ret
colors=[-1]*N
colors[0]=0
ans=check(colors,1,orders,3)
print(ans)
