N=int(input())
array=list(map(int, input().split()))
dp=[pow(10,20)]*N
dp[0]=array[0]
dp[1]=array[0]
for i in range(1,N):
    a=array[i]
    dp[i]=min(dp[i],dp[i-1]+a)
    if i+1<N:
        dp[i+1]=min(dp[i+1],dp[i-1]+a)
ret1=dp[-1]

array=array[-1:]+array[:-1]
dp=[pow(10,20)]*N
dp[0]=array[0]
dp[1]=array[0]
for i in range(1,N):
    a=array[i]
    dp[i]=min(dp[i],dp[i-1]+a)
    if i+1<N:
        dp[i+1]=min(dp[i+1],dp[i-1]+a)
ret2=dp[-1]
print(min(ret1,ret2))
