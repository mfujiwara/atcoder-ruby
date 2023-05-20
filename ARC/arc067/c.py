import collections
MOD=pow(10,9)+7
N,A,B,C,D=map(int, input().split())
binom=[[0]*(N+1) for _ in range(N+1)]
binom[0][0]=1
fn=[1,1]
inv=[1,1]
inv_fn=[1,1]
for i in range(2,N+1):
    fn.append(fn[-1]*i%MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    inv_fn.append(inv_fn[-1]*inv[-1]%MOD)
for i in range(1,N+1):
    binom[i][0]=1
    binom[i][i]=1
    for j in range(i-1):
        binom[i][j+1]=(binom[i-1][j]+binom[i-1][j+1])%MOD
dp=collections.defaultdict(int) # dp[i]:=残り人数iの場合の数
dp[N]=1
ret=0
for i in range(B,A-1,-1):
    nexts=collections.defaultdict(int)
    for key,v in dp.items():
        nexts[key]=v
    for key, v in dp.items():
        for j in range(C,D+1):
            nkey=key-i*j
            if nkey<0:
                break
            val=v*fn[key]%MOD
            val=val*inv_fn[key-i*j]%MOD
            val=val*pow(inv_fn[i],j,MOD)%MOD
            val=val*inv_fn[j]%MOD
            if nkey==0:
                ret+=val
                ret%=MOD
            elif nkey>0:
                nexts[nkey]+=val
                nexts[nkey]%=MOD
    dp=nexts
print(ret)
