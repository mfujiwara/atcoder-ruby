import heapq
N,M=map(int, input().split())
C=[[0]*M for _ in range(N)]
for i in range(N):
    for j,ch in enumerate(input()):
        if ch=="s":
            sx,sy=i,j
            C[i][j]=10
        elif ch=="g":
            gx,gy=i,j
        elif ch=="#":
            continue
        else:
            C[i][j]=int(ch)
done=[[False]*M for _ in range(N)]
shortest=[[10]*M for _ in range(N)]
shortest[gx][gy]=-10
queue=[(-10, gx, gy)]
heapq.heapify(queue)

while len(queue)>0:
    cost, ux, uy = heapq.heappop(queue)
    if shortest[ux][uy]<cost: continue
    done[ux][uy] = True    #探されたuは確定

    for vx,vy in [(ux+1,uy),(ux-1,uy),(ux,uy+1),(ux,uy-1)]:
        if not(0<=vx<N and 0<=vy<M and C[vx][vy]!=0): continue 
        if done[vx][vy]: continue
        a = max(shortest[ux][uy]*0.99,-C[vx][vy])
        if a < shortest[vx][vy]:
            shortest[vx][vy]=a
            heapq.heappush(queue, (a,vx,vy))
if shortest[sx][sy]==10:
    print(-1)
else:
    print(-shortest[sx][sy])
