N=int(input())
S=input()
dp=[[0]*(N+1) for _ in range(N+1)]
ret=0
for i in range(N-2,-1,-1):
    for j in range(N-1,i+1,-1):
        if S[i]==S[j]:
            dp[i][j]=min(dp[i+1][j+1]+1,j-i)
            ret=max(ret,dp[i][j])
print(ret)
