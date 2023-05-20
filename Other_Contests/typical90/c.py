from collections import defaultdict
def max_distance_and_index(start, edges):
    distances=[-1]*N
    distances[start]=0
    targets=[start]
    rets=(0,start) # distance, index
    while targets:
        t=targets.pop()
        for u in edges[t]:
            if distances[u]==-1:
                distances[u]=distances[t]+1
                targets.append(u)
                if distances[u]>rets[0]:
                    rets=(distances[u],u)
    return rets
N=int(input())
edges=defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
_,s=max_distance_and_index(0,edges)
dist,_=max_distance_and_index(s,edges)
print(dist+1)
