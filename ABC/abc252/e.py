import collections
import heapq
N,M=map(int, input().split())
edges=collections.defaultdict(list)
for i in range(M):
    i+=1
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    edges[a].append((c,b,i))
    edges[b].append((c,a,i))
targets=[]
for cabi in edges[0]:
    heapq.heappush(targets,cabi)
done=[False]*N
done[0]=True
rets=[]
while len(rets)<N-1:
    c,b,i=heapq.heappop(targets)
    if not done[b]:
        done[b]=True
        rets.append(i)
        for cc,bb,ii in edges[b]:
            if not done[bb]:
                heapq.heappush(targets,(c+cc,bb,ii))
print(*rets)
