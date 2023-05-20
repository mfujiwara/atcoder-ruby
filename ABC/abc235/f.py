MOD=998244353
N=input()
M=int(input())
array=list(map(int, input().split()))
mask=0
for a in array:
    mask+=pow(2,a)

digits=0  # set(N[:i]) をbitで表したもの
Spre=0  # int(N[:i])%MOD
dps=[0]*1024  # 総和
dpc=[0]*1024  # 個数
for i,c in enumerate(N):
    c=int(c)
    new_dpc=[0]*1024
    new_dps=[0]*1024
    # 既に上の桁がある場合
    for m in range(1,1024):
        for d in range(10):
            # i番目の桁をdにした場合、
            new_dpc[m|1<<d]+=dpc[m] # 遷移前の個数を足す
            new_dps[m|1<<d]+=dps[m]*10+dpc[m]*d # 遷移前の総和x10と今回の総和
    # この桁から開始の場合
    if i:
        for d in range(1,10):
            new_dpc[1<<d]+=1
            new_dps[1<<d]+=d
    # 未満のもの
    for d in range(not i,c):
        new_dpc[digits|1<<d]+=1
        new_dps[digits|1<<d]+=Spre*10+d
 
    for m in range(1,1024):
        dpc[m]=new_dpc[m]%MOD
        dps[m]=new_dps[m]%MOD
    digits|=1<<c
    Spre=(Spre*10+c)%MOD

ret=sum(dps[m] for m in range(1024) if (m&mask)==mask)
if (digits&mask)==mask: ret+=Spre

print(ret%MOD)
