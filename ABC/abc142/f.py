import collections
N,M=map(int, input().split())
count=[0]*N
edges=collections.defaultdict(list)
r_edges=collections.defaultdict(list)
matrix=[[False]*N for _ in range(N)] 
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    r_edges[b].append(a)
    count[b]+=1
    matrix[a][b]=True
targets=[]
for i in range(N):
    if count[i]==0:
        targets.append(i)
while targets:
    t=targets.pop()
    for u in edges[t]:
        count[u]-=1
        r_edges[u].remove(t)
        if count[u]==0:
            targets.append(u)
    edges[t]=[]
now=-1
for i in range(N):
    if count[i]!=0:
        now=i
        break
if now==-1:
    print(-1)
    exit()
rets=[]
while  now not in rets:
    rets.append(now)
    now=r_edges[now][0]
i=rets.index(now)
rets=rets[i:][::-1]
def check(array):
    for i in range(len(array)):
        for j in range(len(array)-2):
            k=(i-j-1+len(array))%len(array)
            if matrix[array[i]][array[k]]:
                if i<k:
                    return array[k:]+array[:i+1]
                else:
                    return array[k:i+1]
    return array
while True:
    tmp=check(rets)
    if tmp==rets:
        break
    else:
        rets=tmp
print(len(rets))
for ret in rets:
    print(ret+1)
