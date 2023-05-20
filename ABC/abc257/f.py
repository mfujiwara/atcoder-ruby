INF=pow(10,10)
N,M=map(int, input().split())
edges=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    if u==-1:
        u==N
    edges[u].append(v)
    edges[v].append(u)
# 0からのコスト
targets=[0]
done=[False]*(N+1)
costs=[INF]*(N+1)
done[0]=True
costs[0]=0
while targets:
    nexts=[]
    for t in targets:
        for u in edges[t]:
            if done[u]: continue
            done[u]=True
            costs[u]=costs[t]+1
            nexts.append(u)
    targets=nexts
# N-1からのコスト
targets=[N-1]
done=[False]*(N+1)
costs1=[INF]*(N+1)
done[N-1]=True
costs1[N-1]=0
while targets:
    nexts=[]
    for t in targets:
        for u in edges[t]:
            if done[u]: continue
            done[u]=True
            costs1[u]=costs1[t]+1
            nexts.append(u)
    targets=nexts
# print(costs)
# print(costs1)
rets=[]
for i in range(N):
    ret=costs[N-1]
    ret1=costs[i]+costs1[N]
    ret2=costs[N]+costs1[i]
    rets.append(min(ret,ret1,ret2))
print(*[ret if ret<INF else -1 for ret in rets])
