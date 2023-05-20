N,K=map(int, input().split())
array=list(map(int, input().split()))
dp=[0]*(N+1)
for i in range(1,N+1):
    if i in array:
        dp[i]=i
    else:
        ret=0
        for a in array:
            if a<i:
                ret=max(ret,i-dp[i-a])
        dp[i]=ret
print(dp[-1])
