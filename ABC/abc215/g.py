import collections
MOD=998244353
N=int(input())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,N+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
def comb(n,k):
    if n<k:
        return 0
    return fn[n]*fn_inv[k]%MOD*fn_inv[n-k]%MOD
array=list(map(int, input().split()))
# counts[i]:=色iのキャンディの数
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
# ccounts[i]:=同色がi個ある色の種類数
ccounts=collections.defaultdict(int)
for v in counts.values():
    ccounts[v]+=1
for k in range(1,N+1):
    ret=0
    base=comb(N,k)
    for key,val in ccounts.items():
        ret+=(base-comb(N-key,k))%MOD*val%MOD
        ret%=MOD
    ret=ret*fn_inv[N]%MOD*fn[k]%MOD*fn[N-k]%MOD
    print(ret)
