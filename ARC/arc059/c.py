import collections


MOD=pow(10,9)+7
N,C=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
x_sums=[[0] for _ in range(C+1)] # x_sums[i][j]:= 1^i+..+j^i
for j in range(1,max(b_array)+1):
    x=1
    for i in range(C+1):
        x_sums[i].append((x_sums[i][-1]+x)%MOD)
        x*=j
        x%=MOD
#print(x_sums)
dp=[[0]*(C+1) for _ in range(N)] # dp[i][j]:= 子供iまででj個あげた場合の活発度
for i in range(N):
    a=a_array[i]
    b=b_array[i]
    if i==0:
        for j in range(C+1):
            dp[i][j]+=(x_sums[j][b]-x_sums[j][a-1])%MOD
        continue
    for j in range(C+1):
        for k in range(j+1):
            dp[i][j]+=dp[i-1][k]*(x_sums[j-k][b]-x_sums[j-k][a-1])%MOD
            dp[i][j]%=MOD
print(dp[-1][-1])
#print(dp)