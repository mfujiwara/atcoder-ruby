H,W,K=map(int, input().split())
A=[[0]*W for _ in range(H)]
start_x=-1
start_y=-1
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="#":
            A[i][j]=1
        elif ch=="S":
            start_x=i
            start_y=j
mini=min([start_x,H-1-start_x,start_y,W-1-start_y])
targets=[(start_x,start_y)]
A[start_x][start_y]=2
for _ in range(K):
    nexts=[]
    for x,y in targets:
        if x>0 and A[x-1][y]==0:
            A[x-1][y]=2
            nexts.append((x-1,y))
            mini=min(mini,x-1)
        if x<H-1 and A[x+1][y]==0:
            A[x+1][y]=2
            nexts.append((x+1,y))
            mini=min(mini,H-1-x-1)
        if y>0 and A[x][y-1]==0:
            A[x][y-1]=2
            nexts.append((x,y-1))
            mini=min(mini,y-1)
        if y<W-1 and A[x][y+1]==0:
            A[x][y+1]=2
            nexts.append((x,y+1))
            mini=min(mini,W-1-y-1)
    targets=nexts
print(1+(mini+K-1)//K)
