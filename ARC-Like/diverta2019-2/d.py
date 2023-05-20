N=int(input())
g1,s1,b1=map(int, input().split())
g2,s2,b2=map(int, input().split())
dp=[0]*(N+1)
for a1,a2 in [(g1,g2),(s1,s2),(b1,b2)]:
    if a1>=a2: continue
    for i in range(N+1-a1):
        dp[i+a1]=max(dp[i+a1],dp[i]+a2)
mid=N
for i in range(N+1):
    mid=max(mid,N-i+dp[i])
dp=[0]*(mid+1)
for a1,a2 in [(g2,g1),(s2,s1),(b2,b1)]:
    if a1>=a2: continue
    for i in range(mid+1-a1):
        dp[i+a1]=max(dp[i+a1],dp[i]+a2)
ret=mid
for i in range(mid+1):
    ret=max(ret,mid-i+dp[i])
print(ret)
