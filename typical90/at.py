N=int(input())
dp=[[0]*46 for _ in range(3)]
for i in range(3):
    array=list(map(int, input().split()))
    for a in array:
        dp[i][a%46]+=1
ret=0
for i in range(46):
    for j in range(46):
        ret+=dp[0][i]*dp[1][j]*dp[2][(92-i-j)%46]
print(ret)
