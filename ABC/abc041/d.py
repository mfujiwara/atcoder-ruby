import collections
N,M=map(int, input().split())
parents=collections.defaultdict(list)
for _ in range(M):
    x,y=map(int, input().split())
    parents[y-1].append(x-1)
dp=[0]*(2**N)
dp[0]=1
for bit in range(2**N):
    already=[]
    yet=[]
    for i in range(N):
        if bit&(1<<i)!=0:
            already.append(i)
        else:
            yet.append(i)
    for i in yet:
        if all([parent in already for parent in parents[i]]):
            dp[bit|(1<<i)]+=dp[bit]
print(dp[-1])
