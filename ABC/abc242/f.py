MOD=998244353
N,M,B,W=map(int, input().split())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,N*M+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
# dp1[i][j]:=ちょうどi*j使ってB個置く場合の数
dp1=[[0]*(M+1) for _ in range(N+1)]
# dp2[i][j]:=i*jより小さく使ってW個置く場合の数
dp2=[[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(M+1):
        if i*j>=B:
            v=fn[i*j]*fn_inv[B]%MOD*fn_inv[i*j-B]%MOD
            for i1 in range(i+1):
                for j1 in range(j+1):
                    v1=dp1[i1][j1]
                    v1*=fn[i]*fn_inv[i-i1]%MOD*fn_inv[i1]%MOD
                    v1*=fn[j]*fn_inv[j-j1]%MOD*fn_inv[j1]%MOD
                    v-=v1
                    v%=MOD
            dp1[i][j]=v
        if i*j>=W:
            v=fn[i*j]*fn_inv[W]%MOD*fn_inv[i*j-W]%MOD
            dp2[i][j]=v
# print(dp1)
# print(dp2)
ret=0
for i in range(1,N):
    for j in range(1,M):
        # i*jの領域にB個、それ以外にW個置く場合の数
        ci=fn[N]*fn_inv[i]%MOD*fn_inv[N-i]%MOD
        cj=fn[M]*fn_inv[j]%MOD*fn_inv[M-j]%MOD
        c=ci*cj%MOD
        v=c*dp1[i][j]%MOD*dp2[N-i][M-j]
        ret+=v
        ret%=MOD
print(ret)
