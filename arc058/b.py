MOD=pow(10,9)+7
H,W,A,B=map(int, input().split())
# (H+W-2)_C_(H-1)
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,H+W+1):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
# ((-A + B + H + x - 2)! (A - B + W - x - 1)!)/((B - 1)! (A - x)! (-B + W - 1)! (-A + H + x - 1)!)
ret=0
for x in range(1,A+1):
    r=fn[-A+B+H+x-2]
    r=r*fn[A-B+W-x-1]%MOD
    r=r*fn_inv[B-1]%MOD
    r=r*fn_inv[A-x]%MOD
    r=r*fn_inv[-B+W-1]%MOD
    r=r*fn_inv[-A+H+x-1]%MOD
    ret+=r
    ret%=MOD
total=fn[H+W-2]
total=total*fn_inv[H-1]%MOD
total=total*fn_inv[W-1]%MOD
print((MOD+total-ret)%MOD)
