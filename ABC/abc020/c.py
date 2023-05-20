import sys
import heapq
H,W,T=map(int, input().split())
MAP=[input() for _ in range(H)]
s=None
g=None
for i in range(H):
    for j in range(W):
        if MAP[i][j]=="S":
            s=(i,j)
        elif MAP[i][j]=="G":
            g=(i,j)
l=1
r=T
while True:
    if l+1==r:
        print(l)
        sys.exit()
    mid=(l+r)//2
    costs=[[-1]*W for _ in range(H)]
    targets=[(0,s[0],s[1])]
    heapq.heapify(targets)
    while targets:
        t,i,j = heapq.heappop(targets)
        if costs[i][j]!=-1: continue
        costs[i][j]=t
        if (i,j)==g:
            break
        if i>0 and costs[i-1][j]==-1:
            if MAP[i-1][j]=="#":
                heapq.heappush(targets,(t+mid,i-1,j))
            else:
                heapq.heappush(targets,(t+1,i-1,j))
        if i<H-1 and costs[i+1][j]==-1:
            if MAP[i+1][j]=="#":
                heapq.heappush(targets,(t+mid,i+1,j))
            else:
                heapq.heappush(targets,(t+1,i+1,j))
        if j>0 and costs[i][j-1]==-1:
            if MAP[i][j-1]=="#":
                heapq.heappush(targets,(t+mid,i,j-1))
            else:
                heapq.heappush(targets,(t+1,i,j-1))
        if j<W-1 and costs[i][j+1]==-1:
            if MAP[i][j+1]=="#":
                heapq.heappush(targets,(t+mid,i,j+1))
            else:
                heapq.heappush(targets,(t+1,i,j+1))
    if costs[g[0]][g[1]]<=T:
        l=mid
    else:
        r=mid
