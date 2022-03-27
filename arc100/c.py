N=int(input())
array=list(map(int, input().split()))
dp=[[None]*(30) for _ in range(pow(2,N))]
for i in range(pow(2,N)):
    dp[i][0]=[array[i]]
for j in range(29):
    for i in range(pow(2,N)):
        if i&(1<<j)!=0:
            dp[i][j+1]=dp[i&~(1<<j)][j]+dp[i][j]
            dp[i][j+1].sort(reverse=True)
            dp[i][j+1]=dp[i][j+1][:2]
        else:
            dp[i][j+1]=dp[i][j]
ret=0
for i in range(1,pow(2,N)):
    ret=max(ret,sum(dp[i][-1]))
    print(ret)
