import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
Q=int(input())
vdc=[]
for _ in range(Q):
    v,d,c=map(int, input().split())
    vdc.append((v-1,d,c))
dd=[-1]*N
rets=[0]*N
while vdc:
    v,d,c=vdc.pop()
    queue=collections.deque([(v,d,c)])
    while queue:
        nv,nd,nc=queue.popleft()
        if rets[nv]==0:
            rets[nv]=nc
        if dd[nv]>=nd or nd==0:
            continue
        dd[nv]=nd
        for u in edges[nv]:
            queue.append((u,nd-1,nc))
print(*rets,sep="\n")
