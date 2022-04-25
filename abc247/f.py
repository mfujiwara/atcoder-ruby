import functools
MOD=998244353
N=int(input())
p_array=list(map(int, input().split()))
q_array=list(map(int, input().split()))
p_array=[(a,i) for i,a in enumerate(p_array)]
p_array.sort()
array=[0]*N
for i in range(N):
    _,index=p_array[i]
    array[i]=q_array[index]-1
ret=1
done=[False]*N
#print(*array)
@functools.lru_cache(maxsize=None)
def calc(n):
    dp=[0]*(n)
    dp1=[0]*(n)
    dp[0]=1
    dp[1]=2
    dp1[1]=1
    for i in range(2,n):
        dp[i]=(dp[i-1]+dp[i-2])%MOD
        dp1[i]=(dp1[i-1]+dp1[i-2])%MOD
    #print(n,dp,dp1)
    return (dp[-1]+dp1[-1])%MOD
for i in range(N):
    t=i
    c=0
    while not done[t]:
        c+=1
        done[t]=True
        t=array[t]
    if c>1:
        ret*=calc(c)
        ret%=MOD
print(ret)
# 2->3
1234
2341
123
231