MOD=998244353
N=int(input())
X=input()
# 全体の候補の数
cnt=(int(X,2)+1)%MOD
ret=0
minusls=[0]*(N+1)
for i in range(3,N+1,2)[::-1]:
    # 2N操作した時に2i周期のものを探す
    if N%i!=0:
        continue
    loop=N//i
    # c個ある
    c=int(X[:loop],2)
    y=bin(2**loop-c-1)[2:].zfill(loop)
    if (X[:loop]+y)*(i//2)+X[:loop]<=X:
        # 最初のloop文字が等しいものが範囲内なら+1
        c+=1
    # 包除原理
    for j in range(i*3,N+1,i):
        c-=minusls[j]
    minusls[i]=c
    # 2Nじゃないと確定した数だけ引く
    cnt-=c
    cnt%=MOD
    ret+=c*2*loop
    ret%=MOD
ret+=cnt*2*N%MOD
ret%=MOD
print(ret)
