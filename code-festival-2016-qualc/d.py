H,W=map(int, input().split())
ord_a=ord("a")
C=[list(map(lambda e: ord(e)-ord_a, list(input()))) for _ in range(H)]
ret=0
for w in range(W-1):
    # memo[i][j]:=隣合うブロックがi個j個残っているときにどちらかを沈めるときにかかるコスト
    memo=[[0]*(H+1) for _ in range(H+1)]
    for i in range(1,H+1):
        for j in range(1,H+1):
            memo[i][j]=memo[i-1][j-1]+(C[i-1][w]==C[j-1][w+1])
    # dp[i][j]:=隣合うブロックがi個j個残っているときに完全に沈めるまでの最低コスト
    dp=[[0]*(H+1) for _ in range(H+1)]
    for i in range(1,H+1):
        for j in range(1,H+1):
            dp[i][j]=memo[i][j]+min(dp[i-1][j],dp[i][j-1])
    ret+=dp[-1][-1]
print(ret)
