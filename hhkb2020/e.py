MOD=10**9+7
ppows=[1]
H,W=map(int, input().split())
MAP=[input() for _ in range(H)]
count=0
left=[[0]*W for _ in range(H)]
right=[[0]*W for _ in range(H)]
up=[[0]*W for _ in range(H)]
down=[[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if MAP[i][j]==".":
            count+=1
            ppows.append(ppows[-1]*2%MOD)
            if i>0:
                down[i][j]+=(down[i-1][j]+1)
            else:
                down[i][j]=1
            if j>0:
                right[i][j]+=(right[i][j-1]+1)
            else:
                right[i][j]=1
        
        ri=H-i-1
        rj=W-j-1
        if MAP[ri][rj]==".":
            if ri<H-1:
                up[ri][rj]+=(up[ri+1][rj]+1)
            else:
                up[ri][rj]=1
            if rj<W-1:
                left[ri][rj]+=(left[ri][rj+1]+1)
            else:
                left[ri][rj]=1
all=ppows[-1]
ret=0
for i in range(H):
    for j in range(W):
        if MAP[i][j]=="#": continue
        c=left[i][j]+right[i][j]+up[i][j]+down[i][j]-3
        ret+=(all-ppows[count-c]+MOD)
        ret%=MOD
print(ret)
