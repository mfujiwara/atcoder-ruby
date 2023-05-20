MOD=998244353
N,M=map(int, input().split())

p=[0]*(N) # p[i]:=M^i
p[0]=1
for i in range(1,N):
    p[i]=p[i-1]*M%MOD

dp1=[[0]*N for _ in range(M+1)] # dp1[i][j]:= "A_j=i"としたときに追加作業が必要な数
dp2=[[0]*N for _ in range(M+1)] # dp2[i][j]:= "A_j=i"としたときに追加作業が不要な数
ret=0
for i in range(1,M+1):
    # A_0=i とするので必ず作業が必要
    dp1[i][0]=1
    # 残りのindexは自由
    ret+=dp1[i][0]*p[N-1]%MOD
    ret%=MOD
    for j in range(1,N):
         # 1つ前のindexで作業が必要になるもののうち、iを選ぶ1通りだけ追加作業が不要になる
         # 1つ前のindexで作業が不要になるもののうち、i以下を選ぶi通りで追加作業が不要になる
        dp1[i][j]=(dp1[i][j-1]*(M-1)+dp2[i][j-1]*(M-i))%MOD
        dp2[i][j]=(dp1[i][j-1]+dp2[i][j-1]*i)%MOD
        # 残りのindexは自由
        ret+=dp1[i][j]*p[N-j-1]%MOD
        ret%=MOD
print(ret)
