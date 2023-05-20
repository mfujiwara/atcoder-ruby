import collections
MOD=pow(10,9)+7
N=int(input())
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,N+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
targets=[0]
status=[0]*N
status[0]=1
dp=[1]*N # ルートから見た場合の数
counts=[0]*N # ルートから見た子供の数
while targets:
    t=targets.pop()
    if status[t]==1:
        status[t]=2
        targets.append(t)
        for u in edges[t]:
            if status[u]!=0: continue
            status[u]=1
            targets.append(u)
    else:
        status[t]=3
        num=1
        count=0
        for u in edges[t]:
            if status[u]!=3: continue
            num*=dp[u]
            num%=MOD
            num*=fn_inv[counts[u]]
            num%=MOD
            count+=counts[u]
        dp[t]=num*fn[count]%MOD
        counts[t]=count+1
targets=[0]
rets=[0]*N
rets[0]=dp[0]
while targets:
    t=targets.pop()
    for u in edges[t]:
        if rets[u]!=0: continue
        # rets[t'] = rets[t] / dp[u] * fn[counts[u]] * fn_inv[N] * fn[N-1-counts[u]]
        #  = rets[t]*counts[u]*pow(N-counts[u],MOD-2,MOD) * fn[counts[u]-1]*fn_inv[N]*fn[N-1-counts[u]]
        # rets[t']* fn_inv[counts[u]-1]*fn[N]*fn_inv[N-1-counts[u]] *dp[u] = rets[t]
        rets[u]=rets[t]*counts[u]*pow(N-counts[u],MOD-2,MOD)%MOD
        targets.append(u)
for ret in rets:
    print(ret)
