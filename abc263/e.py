MOD=998244353
N=int(input())
inv=[1,1]
for n in range(2,N+1):
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    #inv.append(1/n)
array=list(map(int, input().split()))
dp=[0]
sums=[0]
for i in range(1,N):
    a=array[N-1-i]
    # v=0
    # for k in range(1,a+1):
    #     v+=(dp[-k]+1)*inv[a+1]
    # v%=MOD
    vv=(a+sums[-1]-(sums[-a-1] if a<len(sums) else 0))*inv[a+1]%MOD
    #print("v",v,vv)
    #print(v,a,inv[a],inv[a+1])
    # x=v+(x+1)/(a+1)
    # x*(a+1)=v*(a+1)+x+1
    # ax=v*(a+1)+1
    x=(vv*(a+1)%MOD+1)*inv[a]%MOD
    dp.append(x%MOD)
    sums.append((sums[-1]+dp[-1])%MOD)
print(dp[-1])
