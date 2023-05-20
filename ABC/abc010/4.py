import collections
N,G,E=map(int, input().split())
array=list(map(int, input().split()))
edges=[[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    a,b=map(int, input().split())
    edges[a][b]+=1
    edges[b][a]+=1
for a in array:
    edges[a][N]+=1
def calc():
    targets=collections.deque([(0,tuple([0]))])
    done=[False]*(N+1)
    done[0]=True
    while targets:
        t,paths=targets.popleft()
        for u,v in enumerate(edges[t]):
            if v==0 or done[u]: continue
            if u==N:
                return list(paths)+[u]
            targets.append((u,tuple(list(paths)+[u])))
            done[u]=True
    return []
ret=0
while True:
    path=calc()
    if len(path)==0:
        break
    ret+=1
    for i in range(len(path)-1):
        a=path[i]
        b=path[i+1]
        edges[a][b]-=1
        edges[b][a]+=1
print(ret)
