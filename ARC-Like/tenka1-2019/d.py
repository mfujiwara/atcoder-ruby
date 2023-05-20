import collections
MOD=998244353
N=int(input())
array=[int(input()) for _ in range(N)]
total=sum(array)
upper=total//2+1 # 最初の個別NG
# dp[i]:=赤が合計iになる場合の数
dp=[0]*(upper+1)
dp[0]=1
dp2=[0]*(upper+1)
dp2[0]=1
for a in array:
    nexts=[0]*(upper+1)
    nexts2=[0]*(upper+1)
    for l,val in enumerate(dp):
        nexts[l]+=val*2%MOD
        nexts[l]%=MOD
        nexts[min(l+a,upper)]+=val
        nexts[min(l+a,upper)]%=MOD
    dp=nexts
    for l,val in enumerate(dp2):
        nexts2[l]+=val
        nexts2[l]%=MOD
        nexts2[min(l+a,upper)]+=val
        nexts2[min(l+a,upper)]%=MOD
    dp2=nexts2
# print(total,upper)
# print(dp)
# print(dp2)
# print(pow(3,N,MOD))
impossible_count=dp[upper]*3%MOD
if total%2==0:
    impossible_count+=dp[upper-1]*3%MOD
    impossible_count%=MOD
    impossible_count-=dp2[upper-1]*3%MOD
    impossible_count%=MOD
ret=pow(3,N,MOD)-impossible_count
ret%=MOD
print(ret)
