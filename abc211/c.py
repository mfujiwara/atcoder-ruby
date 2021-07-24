MOD=10**9+7
S=input()
dp=[0]*9
dp[0]=1
for ch in S:
    if ch=="c":
        dp[1]+=dp[0]
    elif ch=="h":
        dp[2]+=dp[1]
    elif ch=="o":
        dp[3]+=dp[2]
    elif ch=="k":
        dp[4]+=dp[3]
    elif ch=="u":
        dp[5]+=dp[4]
    elif ch=="d":
        dp[6]+=dp[5]
    elif ch=="a":
        dp[7]+=dp[6]
    elif ch=="i":
        dp[8]+=dp[7]
print(dp[-1]%MOD)
