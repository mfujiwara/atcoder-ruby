import collections
import bisect
import sys
sys.setrecursionlimit(500000)
INF=pow(10,10)
N=int(input())
array=list(map(int, input().split()))
edges=collections.defaultdict(list)
for _ in range(N-1):
    u,v=map(int, input().split())
    u,v=u-1,v-1
    edges[u].append(v)
    edges[v].append(u)
done=[False]*N
lis=[INF]*N
rets=[-1]*N
def calc(now):
    done[now]=True
    i=bisect.bisect_left(lis,array[now])
    changed=False
    if lis[i]!=array[now] and lis[i]>array[now]:
        lis[i],tmp=array[now],lis[i]
        changed=True
    rets[now]=bisect.bisect_left(lis,INF)
    for n in edges[now]:
        if done[n]: continue
        calc(n)
    if changed:
        lis[i]=tmp
    done[now]=False
calc(0)
for r in rets:
    print(r)
