N=int(input())
dp=[0]*(N+1)
dp[1]=3.5
for i in range(2,N+1):
    total=0
    for k in range(1,7):
        if k<dp[i-1]:
            total+=dp[i-1]
        else:
            total+=k
    dp[i]=total/6
print(dp[N])
