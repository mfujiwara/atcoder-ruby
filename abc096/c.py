H,W=map(int, input().split())
S=[[0]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="#":
            S[i][j]=1
for i in range(H):
    for j in range(W):
        if S[i][j]==1:
            b=False
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<H and 0<=y<W:
                    if S[x][y]==1:
                        b=True
            if not b:
                print("No")
                exit()
print("Yes")
