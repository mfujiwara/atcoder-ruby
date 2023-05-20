MOD=998244353
N=int(input())
array=list(map(int, input().split()))
ret=0
for n in range(1,N+1):
    dp=[[0]*n for _ in range(n+1)]
    dp[0][0]=1
    for a in array:
        a%=n
        for k in range(n,0,-1):
            for i in range(n):
                dp[k][(i+a)%n]+=dp[k-1][i]
                dp[k][(i+a)%n]%=MOD
    ret+=dp[n][0]
    ret%=MOD
print(ret)
