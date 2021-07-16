MOD=10**9+7
S=input()
dp=[[0]*4 for _ in range(len(S)+1)]
dp[0][0]=1
for i,ch in enumerate(S):
    if ch=="A":
        dp[i+1][0]=(dp[i][0])%MOD
        dp[i+1][1]=(dp[i][1]+dp[i][0])%MOD
        dp[i+1][2]=(dp[i][2])%MOD
        dp[i+1][3]=(dp[i][3])%MOD
    elif ch=="B":
        dp[i+1][0]=(dp[i][0])%MOD
        dp[i+1][1]=(dp[i][1])%MOD
        dp[i+1][2]=(dp[i][2]+dp[i][1])%MOD
        dp[i+1][3]=(dp[i][3])%MOD
    elif ch=="C":
        dp[i+1][0]=(dp[i][0])%MOD
        dp[i+1][1]=(dp[i][1])%MOD
        dp[i+1][2]=(dp[i][2])%MOD
        dp[i+1][3]=(dp[i][3]+dp[i][2])%MOD
    else:
        dp[i+1][0]=(dp[i][0]*3)%MOD
        dp[i+1][1]=(dp[i][1]*3+dp[i][0])%MOD
        dp[i+1][2]=(dp[i][2]*3+dp[i][1])%MOD
        dp[i+1][3]=(dp[i][3]*3+dp[i][2])%MOD
print(dp[-1][-1])
