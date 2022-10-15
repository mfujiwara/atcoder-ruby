N,M=map(int, input().split())
d=[]
for i in range(M+1):
    if M-i*i<0:
        break
    j=int(pow(M-i*i,0.5))
    if i*i+j*j==M:
        d.append((i,j))
#print(d)
rets=[[N*N]*N for _ in range(N)]
rets[0][0]=0
targets=[(0,0)]
while targets:
    nexts=[]
    for x,y in targets:
        for i,j in d:
            for sx,sy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                nx=x+i*sx
                ny=y+j*sy
                if 0<=nx<N and 0<=ny<N and rets[nx][ny]==N*N:
                    rets[nx][ny]=rets[x][y]+1
                    nexts.append((nx,ny))
    targets=nexts
for i in range(N):
    for j in range(N):
        if rets[i][j]==N*N:
            rets[i][j]=-1
    print(*rets[i])
