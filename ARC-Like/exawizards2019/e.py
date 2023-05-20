MOD=pow(10,9)+7
B,W=map(int, input().split())
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,B+W):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
inv2=[1]
for n in range(1,B+W):
    inv2.append(inv2[-1]*inv[2]%MOD)
# pq[i]:=i回移動した時にB/Wを選択できない確率
pp=[0]
qq=[0]
for i in range(1,B+W):
    p=0
    if i>=B:
        p=fn[i-1]*fn_inv[B-1]%MOD*fn_inv[i-B]%MOD*inv2[i]%MOD
    pp.append((pp[-1]+p)%MOD)
    q=0
    if i>=W:
        q=fn[i-1]*fn_inv[W-1]%MOD*fn_inv[i-W]%MOD*inv2[i]%MOD
    qq.append((qq[-1]+q)%MOD)
for i in range(B+W):
    r=(1-pp[i]-qq[i])%MOD*inv[2]%MOD
    print((r+qq[i])%MOD)
#print(pp)
#print(qq)
