import collections
N,X=map(int, input().split())
dp=collections.defaultdict(int)
dp[X]=1
for _ in range(N):
    nexts=collections.defaultdict(int)
    array=list(map(int, input().split()))
    for i in range(1,array[0]+1):
        a=array[i]
        for key in dp:
            q,r=divmod(key,a)
            if r==0:
                nexts[q]+=dp[key]
    dp=nexts
print(dp[1])
