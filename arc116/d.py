MOD=998244353
N,M=map(int, input().split())
if M%2==1:
    print(0)
    exit()
fn=[1,1]
inv=[1,1]
inv_fn=[1,1]
for i in range(2,N+1):
    fn.append(fn[-1]*i%MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    inv_fn.append(inv_fn[-1]*inv[i]%MOD)
memo={}
def calc(m,k):
    key=f"{m}_{k}"
    if key in memo:
        return memo[key]
    if k==1:
        if m>N:
            return 0
        else:
            comb=fn[N]
            comb=comb*inv_fn[m]%MOD
            comb=comb*inv_fn[N-m]%MOD
            memo[key]=comb
            return comb
    ret=0
    i=0
    while m-2*i*k>=0 and 2*i<=N:
        comb=fn[N]
        comb=comb*inv_fn[2*i]%MOD
        comb=comb*inv_fn[N-2*i]%MOD
        ret+=calc(m-2*i*k,k//2)*comb%MOD
        i+=1
    memo[key]=ret
    return ret
r=calc(M,pow(2,13))
print(r)
