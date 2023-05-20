N=int(input())
X,Y=map(int, input().split())
ret=N+1
dp=[[0]*(X+1) for _ in range(N+1)] # dp[i][j] i個弁当でj個のたこ焼きを買ったときの最大のたい焼きの数
for i in range(N):
    a,b=map(int, input().split())
    for k in range(i,0,-1):
        for j in range(X,-1,-1):
            if dp[k][j]!=0:
                j2=min(X,a+j)
                dp[k+1][j2]=max(dp[k+1][j2],dp[k][j]+b)
                if j2==X and dp[k+1][j2]>=Y:
                    ret=min(ret,k+1)
    a2=min(X,a)
    dp[1][a2]=max(dp[1][a2],b)
    if a2==X and dp[1][a2]>=Y:
        ret=min(ret,1)
if ret==N+1:
    print(-1)
else:
    print(ret)
