import collections
N,M=map(int, input().split())
array=list(map(int, input().split()))
bonus=collections.defaultdict(int)
for _ in range(M):
    c,y=map(int, input().split())
    bonus[c]=y
dp=[0]
for i in range(N):
    nexts=[0]*(len(dp)+1)
    nexts[0]=max(dp)
    for k,v in enumerate(dp):
        nexts[k+1]=dp[k]+array[i]+bonus[k+1]
    dp=nexts
print(max(dp))
