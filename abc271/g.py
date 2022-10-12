MOD=998244353
def mult(m1, m2):
    n=len(m1)
    ret=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j]+=m1[i][k]*m2[k][j]%MOD
            ret[i][j]%=MOD
    return ret
def ppow(m,n):
    if n==0:
        mm=[[1 if i==j else 0 for j in range(len(m))] for i in range(len(m))]
        return mm
    if n%2==0:
        return ppow(mult(m,m), n//2)
    else:
        return mult(ppow(mult(m,m), n//2),m)
N,X,Y=map(int, input().split())
C=input()
inv_100=pow(100,-1,MOD)
# 24時間アクセスが発生しない確率 q
q=pow(inv_100,24,MOD)
for c in C:
    if c=="T":
        q*=(100-X)
    else:
        q*=(100-Y)
    q%=MOD
# 累積和のベース
qs=pow((1-q)%MOD,-1,MOD)
# M[i][j]:=i時から開始して次のアクセスがj時になる確率
M=[[0]*24 for _ in range(24)]
for i in range(24):
    base=qs
    for k in range(24):
        j=(i+k)%24
        ch=C[j]
        if ch=="T":
            p=X*inv_100%MOD
        else:
            p=Y*inv_100%MOD
        v=base*p%MOD
        M[i][j]=v
        base=base*(1-p)%MOD
    #print(base,qs)
    #print(sum(M[i])%MOD)
#print(*M,sep="\n")
# M2[i][j]:=i時から開始して次の開始がj時（=次のアクセスはj-1時）になる確率
M2=[[0]*24 for _ in range(24)]
for i in range(24):
    for j in range(24):
        M2[i][j]=M[i][(j-1)%24]
# 繰り返し二乗法でiから開始してN回後の開始がj時になる確率を求める
R=ppow(M2,N)
ret=0
for i,ch in enumerate(C):
    if ch=="A":
        ret+=R[0][(i+1)%24]
        ret%=MOD
print(ret)
