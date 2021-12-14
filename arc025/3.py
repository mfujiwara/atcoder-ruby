import collections
import heapq
INF=pow(10,10)
N,M,R,T=list(map(int, input().split()))
h = collections.defaultdict(list)
for _ in range(M):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    h[a].append((b,c))
    h[b].append((a,c))
size=N
ret=0
for start in range(N):
    done=[False]*size
    shortest=[INF]*size
    shortest[start]=0
    pred={}
    queue=[(0, start)]
    heapq.heapify(queue)

    while len(queue)>0:
        cost, u = heapq.heappop(queue)
        if shortest[u]<cost: continue
        done[u] = True    #探されたuは確定

        for v,c in h[u]:
            if done[v]: continue
            a = shortest[u] + c
            if a < shortest[v]:
                shortest[v]=a
                heapq.heappush(queue, (a,v))
                pred[v] = u
    shortest.sort()
    j=1
    for i in range(1,N):
        while j<N and shortest[i]*R>=shortest[j]*T:
            j+=1
        if j==N:
            break
        ret+=N-j
        if i>=j:
            ret-=1
print(ret)
