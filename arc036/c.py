MOD=pow(10,9)+7
N,K=map(int, input().split())
S=input()
# dp[i][j]:=0-1の最大値がi、1-0の最大値がjな場合の数
dp=[[0]*(K+1) for _ in range(K+1)]
dp[0][0]=1
for ch in S:
  nexts=[[0]*(K+1) for _ in range(K+1)]
  for i in range(K):
    for j in range(K+1):
      if ch=="1" or ch=="?":
        nexts[i+1][max(0,j-1)]+=dp[i][j]
        nexts[i+1][max(0,j-1)]%=MOD
      if ch=="0" or ch=="?":
        nexts[max(0,j-1)][i+1]+=dp[j][i]
        nexts[max(0,j-1)][i+1]%=MOD
  dp=nexts
ret=0
for i in range(K+1):
    for j in range(K+1):
        ret=(ret+dp[i][j])%MOD
print(ret)
