MOD=998244353
N,M=map(int, input().split())
A,B,C,D,E,F=map(int, input().split())
walls=set()
for _ in range(M):
    x,y=map(int, input().split())
    walls.add((x,y))
dp=[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0]=1
ret=0
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            x=i*A+j*C+k*E
            y=i*B+j*D+k*F
            if (x,y) in walls: continue
            if i>0:
                dp[i][j][k]+=dp[i-1][j][k]
                dp[i][j][k]%=MOD
            if j>0:
                dp[i][j][k]+=dp[i][j-1][k]
                dp[i][j][k]%=MOD
            if k>0:
                dp[i][j][k]+=dp[i][j][k-1]
                dp[i][j][k]%=MOD
            if i+j+k==N:
                ret+=dp[i][j][k]
                ret%=MOD
print(ret)
