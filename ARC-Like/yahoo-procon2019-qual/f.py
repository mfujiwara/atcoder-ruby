import itertools
MOD=998244353
S=input()
N=len(S)
# 青いボールを持ってる数
array=list(map(int,list(S)))
# 青いボールの数の累積和
b_sums=list(itertools.accumulate(array))
# 赤いボールの数の累積和
r_sums=list(itertools.accumulate([2-a for a in array]))
# dp[i][j]:=i個並べた時に赤いボールをj個使った並び順の場合の数
dp=[[0]*(r_sums[-1]+1) for _ in range(2*N+1)]
dp[0][0] = 1
for i in range(1,2*N+1):
    max_b=min(i,b_sums[min(i-1,N-1)])
    max_r=min(i,r_sums[min(i-1,N-1)])
    min_r=i-max_b
    for j in range(min_r, max_r+1):
        dp[i][j] = dp[i-1][j]
        if j != 0:
            dp[i][j]+=dp[i-1][j-1]
            dp[i][j]%=MOD
print(dp[-1][r_sums[-1]])
