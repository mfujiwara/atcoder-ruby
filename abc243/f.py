import functools
MOD=998244353
N,M,K=map(int, input().split())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,max(N,K)+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
www=[]
for _ in range(N):
    w=int(input())
    www.append(w)
total=sum(www)
w_pow=[[1]*N,www]
total_inv_pow=[1,pow(total,MOD-2,MOD)]
for n in range(2,K+1):
    tmp=[0]*N
    for i in range(N):
        tmp[i]=w_pow[-1][i]*w_pow[1][i]%MOD
    w_pow.append(tmp)
    total_inv_pow.append(total_inv_pow[-1]*total_inv_pow[1]%MOD)
# dp[x][y][z]:= 賞品種類xまでで、y回引いて、z種類あたる確率
dp=[[[0]*(M+1) for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0]=1
for i in range(1,N+1):
    for j in range(K+1):
        for k in range(M+1):
            dp[i][j][k]=dp[i-1][j][k]
            if k>0:
                for jj in range(j):
                    v=dp[i-1][jj][k-1]
                    v*=fn[j]
                    v%=MOD
                    v*=fn_inv[jj]
                    v%=MOD
                    v*=fn_inv[j-jj]
                    v%=MOD
                    v*=w_pow[j-jj][i-1]
                    v%=MOD
                    v*=total_inv_pow[j-jj]
                    v%=MOD
                    dp[i][j][k]+=v
                    dp[i][j][k]%=MOD
print(dp[-1][-1][-1])
