import functools
N,M=map(int, input().split())
XY=[list(map(int, input().split())) for _ in range(N)]
PQ=[list(map(int, input().split())) for _ in range(M)]
L=N+M+1
ddd=[[0]*L for _ in range(L)]
for i in range(L-1):
    for j in range(i+1,L):
        if i==j:
            continue
        if i<N:
            x,y=XY[i]
        elif i<N+M:
            x,y=PQ[i-N]
        else:
            x,y=0,0
        if j<N:
            nx,ny=XY[j]
        elif j<N+M:
            nx,ny=PQ[j-N]
        else:
            nx,ny=0,0
        d=pow(pow(x-nx,2)+pow(y-ny,2),0.5)
        ddd[i][j]=d
        ddd[j][i]=d
dp=[[pow(10,10)]*L for _ in range(1<<(L-1))]
for bit in range(1<<(L-1)):
    for i in range(L):
        if bit==0:
            dp[bit][i]=ddd[L-1][i]
            continue
        for j in range(L):
            if bit&(1<<j):
                if j<N:
                    dp[bit][i]=min(dp[bit][i],dp[bit^(1<<j)][j]+ddd[i][j])
                else:
                    dp[bit][i]=min(dp[bit][i],dp[bit^(1<<j)][j]/2+ddd[i][j])
ret=10**10
for i in range(1<<M):
    i<<=N
    i+=1<<N
    i-=1
    ret=min(ret,dp[i][L-1])
print(ret)
