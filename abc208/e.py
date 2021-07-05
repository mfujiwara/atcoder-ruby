import collections
N,K=map(int, input().split())
NS=list(map(int,list("0" + str(N))))
dp1=[collections.defaultdict(int) for _ in range(len(NS))]
dp=[collections.defaultdict(int) for _ in range(len(NS))]
for i in range(1,len(NS)):
    for key in dp1[i-1]:
        c=dp1[i-1][key]
        new_key=min(K+1,key*NS[i])
        dp1[i][new_key]+=c
        for n in range(NS[i]):
            new_key=min(K+1,key*n)
            dp[i][new_key]+=c
    for key in dp[i-1]:
        c=dp[i-1][key]
        for n in range(10):
            new_key=min(K+1,key*n)
            dp[i][new_key]+=c
    if i==1:
        dp1[i][NS[i]]+=1
        for n in range(1,NS[i]):
            dp[i][n]+=1
    else:
        for n in range(1,10):
            dp[i][n]+=1
ret=0
for key in dp1[-1]:
    if key<=K:
        ret+=dp1[-1][key]
for key in dp[-1]:
    if key<=K:
        ret+=dp[-1][key]
print(ret)
