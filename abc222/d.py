MOD=998244353
N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
dp=[0]*3001
dp[0]=1
for i in range(N):
    nexts=[0]*3001
    total=0
    for j in range(3001):
        total+=dp[j]
        total%=MOD
        if a_array[i]<=j<=b_array[i]:
            nexts[j]=total
    dp=nexts
ret=0
for v in dp:
    ret+=v
    ret%=MOD
print(ret)
