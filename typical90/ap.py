MOD=10**9+7
K=int(input())
if K%9!=0:
    print(0)
    exit()
dp=[0]*(K+1)
for i in range(1,K+1):
    if i<10:
        dp[i]+=1
    for j in range(1,10):
        if i-j<0: break
        dp[i]+=dp[i-j]
        dp[i]%=MOD
print(dp[-1])
