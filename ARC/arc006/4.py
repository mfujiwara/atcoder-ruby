H,W=map(int, input().split())
C=[[False]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="o":
            C[i][j]=True
rets=[0]*3
for i in range(H):
    for j in range(W):
        if C[i][j]:
            size=1
            while C[i][j+size] and C[i+size][j] and C[i+size][j+size]:
                size+=1
            if C[i+size][j+size] and (i+size*4>=H or not C[i+size*4][j-size]):
                rets[0]+=1
            elif i+size*3<H and j+size*3<W and C[i+size*3][j+size*3] and (i+size*4>=H or not C[i+size*4][j+size*3]):
                rets[2]+=1
            else:
                rets[1]+=1
            targets=[(i,j)]
            C[i][j]=False
            while targets:
                x,y=targets.pop()
                for dx in [1,0,-1]:
                    for dy in [1,0,-1]:
                        ux=x+dx
                        uy=y+dy
                        if C[ux][uy]:
                            C[ux][uy]=False
                            targets.append((ux,uy))
print(*rets)
