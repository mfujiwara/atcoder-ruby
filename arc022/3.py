import collections
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
def max_distance(start, edges):
    max_d=0
    max_node=start
    distances=[-1]*len(edges)
    distances[start]=0
    targets=[0,start]
    while targets:
        t=targets.pop()
        for u in edges[t]:
            if distances[u]!=-1: continue
            distances[u]=distances[t]+1
            if distances[u]>max_d:
                max_d=distances[u]
                max_node=u
            targets.append(u)
    return max_node
n1=max_distance(0,edges)
n2=max_distance(n1,edges)
print(f"{n1+1} {n2+1}")
