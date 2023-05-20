MOD=pow(10,9)+7
K=int(input())
S=input()
L=len(S)
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for i in range(2,K+L+1):
    fn.append(fn[-1]*i%MOD)
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    fn_inv.append(fn_inv[-1]*inv[i]%MOD)
ret=0
for i in range(L-1,K+L):
    r=pow(25,i-L+1,MOD)*pow(26,K+L-1-i,MOD)%MOD
    r*=fn[i]
    r%=MOD
    r*=fn_inv[L-1]
    r%=MOD
    r*=fn_inv[i+1-L]
    r%=MOD
    ret+=r
    ret%=MOD
print(ret)
