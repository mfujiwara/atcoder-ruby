H,W=map(int, input().split())
C=[[0]*W for _ in range(H)]
for i in range(H):
    for j,ch in enumerate(input()):
        if ch==".": continue
        C[i][j]=int(ch)
for i in range(H):
    for j in range(W):
        if C[i][j]==0:
            s=set([1,2,3,4,5])
            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                if 0<=i+x<H and 0<=j+y<W and C[i+x][j+y] in s:
                    s.remove(C[i+x][j+y])
            C[i][j]=list(s)[0]
        print(C[i][j],end="")
    print()
