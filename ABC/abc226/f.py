import collections
import math
MOD=998244353
N,K=map(int, input().split())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,N+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
dp=[collections.defaultdict(int) for _ in range(N+1)] # dp[i][j]:= i人いる時のスコアjの場合の数
dp[0][1]=1
for i in range(1,N+1):
    for j in range(1,i+1):
        base=fn[i-1]*fn_inv[i-j]%MOD # 固定要素がjで巡回する場合の数
        for s,c in dp[i-j].items():
            new_s=s*j//math.gcd(s,j)
            dp[i][new_s]+=base*c%MOD
            dp[i][new_s]%=MOD
ret=0
for s,c in dp[N].items():
    ret+=pow(s,K,MOD)*c%MOD
    ret%=MOD
print(ret)
