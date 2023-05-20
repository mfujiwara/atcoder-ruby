import collections
N,M,K=map(int, input().split())
abc=[]
for _ in range(M):
    a,b,c=map(int, input().split())
    abc.append((a,b,c))
array=list(map(int, input().split()))
dp=collections.defaultdict(lambda: pow(10,20))
dp[1]=0
for e in array:
    a,b,c=abc[e-1]
    dp[b]=min(dp[b],dp[a]+c)
    #print(dp)
if dp[N]==pow(10,20):
    print(-1)
else:
    print(dp[N])
