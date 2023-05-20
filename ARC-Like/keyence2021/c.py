MOD=998244353
inv3=332748118
k=inv3*2%MOD
H,W,K=map(int, input().split())
C=[[0]*W for _ in range(H)]
for _ in range(K):
    h,w,c=input().split()
    h=int(h)-1
    w=int(w)-1
    C[h][w]=1 if c=="R" else 2 if c=="D" else 3
dp=[[0]*W for _ in range(H)]
def ppow(x, n):
    if n == 0:
        return 1
    elif (n % 2) == 0:
        return ppow(x**2 % MOD, n // 2)
    elif (n % 2) == 1:
        return ppow(x**2 % MOD, n // 2) * x
dp[0][0]=1
for i in range(H):
    for j in range(W):
        if C[i][j]==1:
            if j<W-1:
                dp[i][j+1]+=dp[i][j]
                dp[i][j+1]%=MOD
        elif C[i][j]==2:
            if i<H-1:
                dp[i+1][j]+=dp[i][j]
                dp[i+1][j]%=MOD
        elif C[i][j]==3:
            if j<W-1:
                dp[i][j+1]+=dp[i][j]
                dp[i][j+1]%=MOD
            if i<H-1:
                dp[i+1][j]+=dp[i][j]
                dp[i+1][j]%=MOD
        else:
            v=dp[i][j]*k%MOD
            if j<W-1:
                dp[i][j+1]+=v
                dp[i][j+1]%=MOD
            if i<H-1:
                dp[i+1][j]+=v
                dp[i+1][j]%=MOD
print(dp[-1][-1]*ppow(3,H*W-K)%MOD)
