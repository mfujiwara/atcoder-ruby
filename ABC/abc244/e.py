import collections
MOD=998244353
N,M,K,S,T,X=map(int, input().split())
S-=1
T-=1
X-=1
edges=collections.defaultdict(list)
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
dp=[[0]*N for _ in range(2)]
dp[0][S]=1
for _ in range(K):
    nexts=[[0]*N for _ in range(2)]
    for start in edges:
        for end in edges[start]:
            if end==X:
                nexts[1][end]=(nexts[1][end]+dp[0][start])%MOD
                nexts[0][end]=(nexts[0][end]+dp[1][start])%MOD
            else:
                nexts[0][end]=(nexts[0][end]+dp[0][start])%MOD
                nexts[1][end]=(nexts[1][end]+dp[1][start])%MOD
    dp=nexts
print(dp[0][T])
