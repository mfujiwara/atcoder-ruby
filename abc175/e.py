R,C,K=map(int, input().split())
V=[[-1]*C for _ in range(R)]
for _ in range(K):
    r,c,v=map(int, input().split())
    V[r-1][c-1]=v
dp=[[0]*C for _ in range(4)]
for i in range(R):
    tmp=[[0]*C for _ in range(4)]
    for j in range(C):
        v=V[i][j]
        dp_max=max(dp[0][j],dp[1][j],dp[2][j],dp[3][j])
        if j==0:
            if v>0:
                tmp[0][j]=dp_max
                tmp[1][j]=dp_max+v
            else:
                tmp[0][j]=dp_max
        else:
            if v>0:
                tmp[0][j]=max(tmp[0][j-1],dp_max)
                tmp[1][j]=max(tmp[0][j-1]+v,tmp[1][j-1],dp_max+v)
                tmp[2][j]=max(tmp[1][j-1]+v,tmp[2][j-1])
                tmp[3][j]=max(tmp[2][j-1]+v,tmp[3][j-1])
            else:
                tmp[0][j]=max(tmp[0][j-1],dp_max)
                tmp[1][j]=tmp[1][j-1]
                tmp[2][j]=tmp[2][j-1]
                tmp[3][j]=tmp[3][j-1]
    dp=tmp
ret=max(dp[0][-1],dp[1][-1],dp[2][-1],dp[3][-1])
print(ret)
