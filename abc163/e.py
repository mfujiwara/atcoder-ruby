N=int(input())
array=list(map(int,input().split()))
dp=[[0]*N for _ in range(N)] # dp[i][j]:= i+1まで確定させて、i人は前に詰めた場合の最大
array=[(a,i) for i,a in enumerate(array)]
array.sort(reverse=True) 
dp[0][0]=array[0][0]*abs(N-1-array[0][1])
dp[0][1]=array[0][0]*array[0][1]
for i in range(1,N):
    for j in range(1,i+1):
        dp[i][j] = max(
            dp[i-1][j]+array[i][0]*abs(N-1-array[i][1]-i+j),
            dp[i-1][j-1]+array[i][0]*abs(array[i][1]-j+1)
        )
    dp[i][0] = dp[i-1][0] + abs(N-1-array[i][1]-i)*array[i][0]
    if i != N-1:
        dp[i][i+1] = dp[i-1][i]+array[i][0]*abs(array[i][1]-i)
print(max(dp[-1]))
