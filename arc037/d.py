MOD=pow(10,9)+7
L=int(input())
line=[0]*(L+3)
line[0]=2
top=[0]*(L+3)
top[0]=1
for i in range(1,L+1):
    top[i]=pow(line[i-1],2,MOD)*top[i-1]-pow(top[i-1],3,MOD)
    top[i]%=MOD
    line[i]=pow(line[i-1],2,MOD)+pow(line[i-1],3,MOD)-pow(top[i-1],2,MOD)*line[i-1]
    line[i]%=MOD 
dp=[0]*(L+4)
dp[1]=11
for i in range(2,L+1):
    dp[i]=3*dp[i-1]+line[i-1]**3
    dp[i]%=MOD
print(dp[L])
