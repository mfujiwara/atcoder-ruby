MOD=998244353
S=input()
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,len(S)+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
counts=[0]*26
ord_a=ord("a")
for ch in S:
    counts[ord(ch)-ord_a]+=1
dp=[0]*(len(S)+1)
dp[0]=1

for count in counts:
    plus=[0]*(len(S)+1)
    for i in range(len(dp)-1-count,-1,-1):
        for c in range(1,count+1):
            plus[i+c]+=((fn[i+c]*fn_inv[c]%MOD)*fn_inv[i]%MOD)*dp[i]%MOD # comb(i+c,c)*dp[i] # (i+c)_C_c
            plus[i+c]%=MOD
    for i in range(len(S)+1):
        dp[i]+=plus[i]
        dp[i]%=MOD
ret=-1
for d in dp:
    ret+=d
    ret%=MOD
print(ret)
