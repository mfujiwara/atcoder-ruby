import heapq
N,M,K=map(int,input().split())
edges=[[] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
a_array=list(map(int,input().split()))
b_array=list(map(int,input().split()))+[-1]
dp=[K+1]*N
dp[0]=int(a_array[0]==b_array[0])
targets=[(dp[0],0)]
while targets:
    d,u = heapq.heappop(targets)
    if d>dp[u]:
        continue
    for v in edges[u]:
        z=d+(a_array[v]==b_array[d])
        if z<dp[v]:
            dp[v]=z
            heapq.heappush(targets,(z,v))
if dp[N-1]==K:
    print("Yes")
else:
    print("No")
