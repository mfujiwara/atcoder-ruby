N=int(input())
array=[]
for i in range(N):
    a=int(input())
    array.append(a)
dp=[[0]*(N+1) for _ in range(N+1)] # dp[i][j]:=[i,j)区間の最大値
for d in range(3,N+1):
    for i in range(N-d+1):
        j=d+i
        for m in range(i+1,j):
            dp[i][j]=max(dp[i][j], dp[i][m]+dp[m][j])
        if d%3==0:
            for m in range(i+1,j,3):
                dp[i][j]=max(dp[i][j],array[i]+dp[i+1][m]+array[m]+dp[m+1][j-1]+array[j-1])
print(dp[0][N])
