MOD=998244353
N,M,K=map(int, input().split())
edges=[[] for _ in range(N)]
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
evens=0
odds=0
for i in range(N):
    if len(edges[i])%2==0:
        evens+=1
    else:
        odds+=1
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,N+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
def combination(n,m):
    if n<m: return 0
    return fn[n]*fn_inv[m]%MOD*fn_inv[n-m]%MOD
e=K
o=0
ret=0
while e>=0:
    ret+=combination(evens,e)*combination(odds,o)%MOD
    ret%=MOD
    e-=2
    o+=2
print(ret)
