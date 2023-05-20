N,M=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
dp=[[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(M+1):
        if i==0 or j==0:
            dp[i][j]= i+j
        else:
            r1=dp[i-1][j]+1
            r2=dp[i][j-1]+1
            r3=dp[i-1][j-1]
            if a_array[i-1]!=b_array[j-1]:
                r3+=1
            dp[i][j]=min(r1,r2,r3)
print(dp[-1][-1])
