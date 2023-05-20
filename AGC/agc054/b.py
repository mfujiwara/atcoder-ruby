import collections
MOD=998244353
N=int(input())
kaijou=[1]
for i in range(1,N+1):
    kaijou.append(kaijou[-1]*i)
W=list(map(int, input().split()))
total=sum(W)
if total%2==1:
    print(0)
    exit()
total//=2
if max(W)>total:
    print(0)
    exit()
dp=[[0]*N for _ in range(total+1)] # dp[i][j]:=j個で重さiになる場合の数
dp[0][0]=1
for w in W:
    for i in range(total-w,-1,-1):
        for index,d in enumerate(dp[i]):
            if index==N-1: continue
            dp[i+w][index+1]+=d
ret=0
for index,d in enumerate(dp[total]):
    r=kaijou[index]*kaijou[N-index]%MOD
    r*=d
    r%=MOD
    ret+=r
    ret%=MOD
print(ret)
