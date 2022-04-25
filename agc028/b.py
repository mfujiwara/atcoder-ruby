MOD=pow(10,9)+7
N=int(input())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,N+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
dp=[0,1]
for i in range(2,N+1):
    dp.append((dp[-1]*(i)%MOD+fn[i-1])%MOD)
countsM=[dp[-2]]
countsN=[dp[-1]]
for i in range(1,(N+1)//2):
    countsN.append((countsM[-1]*N%MOD+fn[N]*inv[i+1]%MOD)%MOD)
    countsM.append((countsN[-1]-(fn[N]*inv[N-i])%MOD)*inv[N]%MOD)
ret=0
array=list(map(int, input().split()))
for i,a in enumerate(array):
    i=min(i,N-1-i)
    ret+=countsN[i]*a%MOD
    ret%=MOD
print(ret)
