import sys
sys.setrecursionlimit(500000)
MOD=10**9+7
H,W=map(int, input().split())
MAP=[]
for i in range(H):
    array=list(map(int, input().split()))
    MAP.append(array)
END_MAP=[[0]*W for _ in range(H)]
def calc(i,j):
    if END_MAP[i][j]!=0:
        return END_MAP[i][j]
    r=1
    if j<W-1 and MAP[i][j+1]<MAP[i][j]:
        r+=calc(i,j+1)
    if i<H-1 and MAP[i+1][j]<MAP[i][j]:
        r+=calc(i+1,j)
    if j>0 and MAP[i][j-1]<MAP[i][j]:
        r+=calc(i,j-1)
    if i>0 and MAP[i-1][j]<MAP[i][j]:
        r+=calc(i-1,j)
    END_MAP[i][j]=r%MOD
    return END_MAP[i][j]
ret=0
for i in range(H):
    for j in range(W):
        ret+=calc(i,j)
        ret%=MOD
print(ret)
