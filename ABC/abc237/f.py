import collections
MOD=998244353
N,M=map(int, input().split())
dp=[[[0]*(M+2) for _ in range(M+2)] for _ in range(M+2)]
dp[M+1][M+1][M+1]=1
for i in range(N):
    nexts=[[[0]*(M+2) for _ in range(M+2)] for _ in range(M+2)]
    for a in range(1,M+2):
        for b in range(1,M+2):
            for c in range(1,M+2):
                for x in range(1,M+1):
                    if x<=a:
                        nexts[x][b][c]+=dp[a][b][c]
                        nexts[x][b][c]%=MOD
                    elif x<=b:
                        nexts[a][x][c]+=dp[a][b][c]
                        nexts[a][x][c]%=MOD
                    elif x<=c:
                        nexts[a][b][x]+=dp[a][b][c]
                        nexts[a][b][x]%=MOD
    dp=nexts
ret=0
for a in range(1,M-1):
    for b in range(a+1,M):
        for c in range(b+1,M+1):
            ret+=dp[a][b][c]
            ret%=MOD
print(ret)
