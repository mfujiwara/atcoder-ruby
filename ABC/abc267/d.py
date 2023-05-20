INF=pow(10,20)
N,M=map(int, input().split())
array=list(map(int, input().split()))
dp=[0]
for i in range(N):
    nexts=dp.copy()
    if len(nexts)<M+1:
        nexts.append(-INF)
    for j in range(min(M,len(dp))):
        nexts[j+1]=max(nexts[j+1],dp[j]+array[i]*(j+1))
    dp=nexts
print(dp[-1])
