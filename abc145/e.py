N,T=map(int, input().split())
ab=[list(map(int, input().split())) for _ in range(N)]
ab=sorted(ab)
dp=[0]*6000
ret=0
for a,b in ab:
    for t in range(T)[::-1]:
        dp[t+a]=max(dp[t+a],dp[t]+b)
        ret=max(ret,dp[t+a])
print(ret)
