N,A=map(int, input().split())
array=list(map(int, input().split()))
array=sorted(array)
dp=[[0]*((i+1)*A+1) for i in range(N)]
for x in array:
    for i in range(N-1)[::-1]:
        for j in range(len(dp[i]))[::-1]:
            if len(dp[i+1])>j+x:
                dp[i+1][j+x]+=dp[i][j]
    if x<=A:
        dp[0][x]+=1
ret=0
for d in dp:
    ret+=d[-1]
print(ret)
