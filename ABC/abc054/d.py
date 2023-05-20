INF=1<<60
N,Ma,Mb=map(int, input().split())
dp=[[INF]*401 for _ in range(401)] # min cost of a,b
dp[0][0]=0
for i in range(N):
    a,b,c=map(int, input().split())
    for i in range(391)[::-1]:
        for j in range(391)[::-1]:
            dp[i+a][j+b]=min(dp[i+a][j+b],dp[i][j]+c)
ret=INF
ma,mb=Ma,Mb
while ma<=400 and mb<=400:
    ret=min(ret,dp[ma][mb])
    ma+=Ma
    mb+=Mb
if ret==INF:
    print(-1)
else:
    print(ret)
