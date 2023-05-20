import bisect
import itertools
N,K=map(int, input().split())
array=[]
for _ in range(N):
    a=int(input())
    array.append(a)
if sum(array)==K:
    print(1)
    exit()
sums=list(itertools.accumulate(array))
# dp[i]:=勝率がi回上がったときの最小の勝利数
INF=pow(10,10)
dp=[0,1]+[INF]*(N-1)
for i in range(1,N):
    # (i+1)日目
    nexts=[0,1]
    for k in range(2,N+1):
        # 直前までの勝率を上回る条件
        # dp[k-1]/sums[i-1] < x/sums[i]
        # x*sums[i-1] > dp[k-1]*sums[i]
        # x > dp[k-1]*sums[i]/sums[i-1]
        x = dp[k-1]*sums[i]//sums[i-1]+1
        if x-dp[k-1]>array[i]:
            x=INF
        nexts.append(min(x,dp[k]))
    dp=nexts
    #print(i,dp)
index=bisect.bisect_right(dp,K)
print(index-1)
