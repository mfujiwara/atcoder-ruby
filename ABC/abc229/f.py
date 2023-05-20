N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
dp=[pow(10,16)]*(N+1) # dp[i]:= i番目が中心と違うグループになるときの最小値
dp[0]=0
for i in range(N):
    dp[i+1]=min(dp[i+1],dp[i]+b_array[i])
    if i<N-1:
        dp[i+2]=min(dp[i+2],dp[i]+a_array[i+1])
    if i<N-2:
        dp[i+3]=min(dp[i+3],dp[i]+a_array[i+1]+a_array[i+2]+b_array[i+1])
ret1=dp[-1]

a_array=a_array[1:]+a_array[:1]
b_array=b_array[1:]+b_array[:1]
dp=[pow(10,16)]*(N+1) # dp[i]:= i番目が中心と違うグループになるときの最小値
dp[0]=0
for i in range(N):
    dp[i+1]=min(dp[i+1],dp[i]+b_array[i])
    if i<N-1:
        dp[i+2]=min(dp[i+2],dp[i]+a_array[i+1])
    if i<N-2:
        dp[i+3]=min(dp[i+3],dp[i]+a_array[i+1]+a_array[i+2]+b_array[i+1])
ret2=dp[-1]
print(min(ret1,ret2))
