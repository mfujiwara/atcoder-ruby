import collections
H,W=map(int, input().split())
A=[list(map(int, input().split())) for _ in range(H)]
B=[list(map(int, input().split())) for _ in range(H)]
dp=[[set() for _ in range(W)] for _ in range(H)]
dp[0][0].add(abs(A[0][0]-B[0][0]))
for i in range(H):
    for j in range(W):
        if i==0 and j==0: continue
        diff=abs(A[i][j]-B[i][j])
        base=set()
        if i>0:
            base|=dp[i-1][j]
        if j>0:
            base|=dp[i][j-1]
        for b in base:
            dp[i][j].add(b+diff)
            dp[i][j].add(abs(b-diff))
ret=min(dp[-1][-1])
print(ret)
