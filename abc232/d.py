H,W=map(int, input().split())
C=[[1]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch=="#":
            C[i][j]=0
for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if C[i][j]==0: continue
        v=0
        if i<H-1:
            v=max(v,C[i+1][j])
        if j<W-1:
            v=max(v,C[i][j+1])
        C[i][j]+=v
print(C[0][0])
