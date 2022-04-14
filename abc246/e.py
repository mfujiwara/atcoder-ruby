N=int(input())
ax,ay=map(int, input().split())
bx,by=map(int, input().split())
ax-=1
ay-=1
bx-=1
by-=1
S=[[-1]*N for _ in range(N)]
for i in range(N):
    for j,ch in enumerate(input()):
        if ch=="#":
            S[i][j]=-2
if (ax+ay)%2!=(bx+by)%2:
    print(-1)
    exit()
targets=[(ax,ay)]
S[ax][ay]=0
while targets:
    nexts=[]
    for x,y in targets:
        for dx,dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for l in range(1,N):
                nx=x+dx*l
                ny=y+dy*l
                if 0<=nx<N and 0<=ny<N and S[nx][ny]!=-2:
                    if S[nx][ny]==-1:
                        S[nx][ny]=S[x][y]+1
                        nexts.append((nx,ny))
                        if nx==bx and ny==by:
                            print(S[nx][ny])
                            exit()
                else:
                    break
    targets=nexts
print(-1)
