import bisect
N,K=map(int, input().split())
array=list(map(int, input().split()))
array.sort()
# dp[i][j]:=i回一斉に抜くことができて低い方からj本残っている時に、個別に抜く必要がある本数
dp=[[K+1]*(N+1) for _ in range(35)]
dp[0][0] = 0
for i in range(1, N+1):
    j=bisect.bisect_right(array, array[i-1]//2)
    dp[0][i]=dp[0][i-1]+1
    for k in range(1,35):
        dp[k][i]=min(dp[k][i-1]+1, dp[k-1][j])
for i in range(35):
    if dp[i][N]<=K:
        print(i,dp[i][N])
        exit()
