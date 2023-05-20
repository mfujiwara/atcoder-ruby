H,W,K=map(int, input().split())
x1,y1,x2,y2=map(int, input().split())
x1-=1
y1-=1
x2-=1
y2-=1
C=[[0]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="@":
            C[i][j]=-1
ret=1
targets=[(x1,y1,0),(x1,y1,1),(x1,y1,2),(x1,y1,3)]
while targets:
    nexts=[]
    for x,y,d in targets:
        if d==0:
            e=[1,0]
        elif d==1:
            e=[0,1]
        elif d==2:
            e=[-1,0]
        else:
            e=[0,-1]
        for k in range(1,K+1):
            ux,uy=x+e[0]*k,y+e[1]*k
            if 0<=ux<H and 0<=uy<W:
                if C[ux][uy]==0:
                    if ux==x2 and uy==y2:
                        print(ret)
                        exit()
                    C[ux][uy]=ret
                    nexts.append((ux,uy,(d+1)%4))
                    nexts.append((ux,uy,(d+3)%4))
                    if k==K:
                        nexts.append((ux,uy,d))
                elif C[ux][uy]<ret:
                    break
            else:
                break
    targets=nexts
    ret+=1
print(-1)
