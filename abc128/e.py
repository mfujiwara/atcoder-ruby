import heapq
N,Q=map(int, input().split())
stx=[]
xt=[]
for _ in range(N):
    s,t,x=map(int, input().split())
    s=s-x
    t=t-x
    heapq.heappush(stx,(s,t,x))
for _ in range(Q):
    d=int(input())
    while stx and stx[0][0]<=d:
        s,t,x=heapq.heappop(stx)
        if t>d:
            heapq.heappush(xt,(x,t))
    while xt and xt[0][1]<=d:
        heapq.heappop(xt)
    if xt:
        print(xt[0][0])
    else:
        print(-1)
