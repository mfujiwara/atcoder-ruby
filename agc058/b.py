MOD=998244353
N=int(input())
array=list(map(int, input().split()))
# do[i]:=0..iまで考慮した時の場合の数
dp=[0]*(N+1)
dp[0]=1
for i in range(N):
    l,r = i,i+1
    while l>0 and array[l-1]<array[i]:
        l -=1
    while r<N and array[r]<array[i]:
        r+=1
    for k in range(l,r):
        dp[k+1]+=dp[k]
        dp[k+1]%=MOD
print(dp[-1])
