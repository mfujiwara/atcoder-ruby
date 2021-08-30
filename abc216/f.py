MOD=998244353
N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
ab=[]
for i in range(N):
    ab.append((a_array[i],b_array[i]))
ab.sort()
dp=[0]*5001
dp[0]=1
ret=0
for a,b in ab:
    if a>=b:
        ret+=sum(dp[:a-b+1])
        ret%=MOD
    for i in range(5001-b-1,-1,-1):
        dp[i+b]+=dp[i]
        dp[i+b]%=MOD
print(ret)
