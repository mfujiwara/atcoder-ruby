import collections
S=input()
K=int(input())
N=len(S)
if N==1:
    print(1)
    exit()
# dp[i][j][k]:=開始位置i、終了位置i+j-1、変更した数kの場合の最大値
dp=[[[0]*(K+1) for _ in range(N+1-i)] for i in range(N)]
for i in range(N):
    dp[i][1][0]=1
for d in range(2,N+1):
    for l in range(N-d+1):
        for k in range(K+1):
            # k-1以上にはなる
            if k>0:
                dp[l][d][k]=max(dp[l][d][k], dp[l][d][k-1])
            # 1つ短い文字列の値以上にはなる
            dp[l][d][k]=max(dp[l][d][k], dp[l][d-1][k], dp[l+1][d-1][k])
            if S[l]==S[l+d-1]:
                # 先頭末尾が同じ場合、除いたものより+2
                dp[l][d][k]=max(dp[l][d][k], dp[l+1][d-2][k]+2)
            else:
                # 先頭末尾が違う場合、除いたものからkを+1すれば+2
                if k>0:
                    dp[l][d][k]=max(dp[l][d][k], dp[l+1][d-2][k-1]+2)
print(dp[0][N][-1])
