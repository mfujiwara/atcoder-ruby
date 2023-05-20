H,W=map(int, input().split())
rs,cs=map(int, input().split())
rt,ct=map(int, input().split())
rs-=1
cs-=1
rt-=1
ct-=1
S=[[0]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="#":
            S[i][j]=1
ret=[[0]*W for _ in range(H)]
ret[rs][cs]=1
ret[rt][ct]=-1
targetsx=[(rs,cs),(rt,ct)]
targetsy=[(rs,cs),(rt,ct)]
INF=1<<60
rrr=INF
while True:
    nextsx=[]
    nextsy=[]
    for x,y in targetsx:
        for nx in range(x-1,-1,-1):
            if S[nx][y]==1: break
            if ret[nx][y]==0:
                if ret[x][y]>0:
                    ret[nx][y]=ret[x][y]+1
                else:
                    ret[nx][y]=ret[x][y]-1
                nextsy.append((nx,y))
            elif ret[nx][y]*ret[x][y]<0:
                rrr=min(rrr,abs(ret[nx][y])+abs(ret[x][y])-2)
        for nx in range(x+1,H):
            if S[nx][y]==1: break
            if ret[nx][y]==0:
                if ret[x][y]>0:
                    ret[nx][y]=ret[x][y]+1
                else:
                    ret[nx][y]=ret[x][y]-1
                nextsy.append((nx,y))
            elif ret[nx][y]*ret[x][y]<0:
                rrr=min(rrr,abs(ret[nx][y])+abs(ret[x][y])-2)
    if rrr<INF:
        break
    for x,y in targetsy:
        for ny in range(y-1,-1,-1):
            if S[x][ny]==1: break
            if ret[x][ny]==0:
                if ret[x][y]>0:
                    ret[x][ny]=ret[x][y]+1
                else:
                    ret[x][ny]=ret[x][y]-1
                nextsx.append((x,ny))
            elif ret[x][ny]*ret[x][y]<0:
                rrr=min(rrr,abs(ret[x][ny])+abs(ret[x][y])-2)
        for ny in range(y+1,W):
            if S[x][ny]==1: break
            if ret[x][ny]==0:
                if ret[x][y]>0:
                    ret[x][ny]=ret[x][y]+1
                else:
                    ret[x][ny]=ret[x][y]-1
                nextsx.append((x,ny))
            elif ret[x][ny]*ret[x][y]<0:
                rrr=min(rrr,abs(ret[x][ny])+abs(ret[x][y])-2)
    if rrr<INF:
        break
    targetsx=nextsx
    targetsy=nextsy
print(rrr)
