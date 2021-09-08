import collections
import heapq
INF=10**18
T=int(input())
for _ in range(T):
    N,A,B,C,D=map(int, input().split())
    done={}
    pred={}
    queue=[-N]
    costs=collections.defaultdict(lambda: INF)
    costs[N]=0
    costs[0]=D*N
    heapq.heapify(queue)

    while len(queue)>0:
        u = heapq.heappop(queue)
        u=-u
        cost=costs[u]
        if u in done:
            continue
        if u==1:
            print(min(cost+D,costs[0]))
            break
        done[u] = True

        costs[0]=min(costs[0],cost+u*D)
        for k,c in [(2,A),(3,B),(5,C)]:
            q,r=divmod(u,k)
            if r==0:
                if q not in done:
                    heapq.heappush(queue,-q)
                    costs[q]=min(costs[q],cost+c)
            else:
                if q not in done:
                    heapq.heappush(queue,-q)
                    costs[q]=min(costs[q],cost+c+D*r)
                if (q+1) not in done:
                    heapq.heappush(queue,-q-1)
                    costs[q+1]=min(costs[q+1],cost+c+D*(k-r))
