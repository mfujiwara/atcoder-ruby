import functools
MOD=998244353
N=int(input())
array=list(map(int, input().split()))
dainari=[[] for _ in range(N)]
for i in range(1,N-1):
    for j in range(i+1,N):
        if array[i]<array[j]:
            dainari[i].append(j)
# dp[i][j]:=iを根にした木でj番目までが子供の要素にいるものの数
dp=[[0]*N for _ in range(N)]
for w in range(N):
    for i in range(N-w):
        j=i+w
        if w<=1:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i+1][j]
            for d in dainari[i+1]:
                if d>j: break
                if i+2==d:
                    dp[i][j]+=dp[i+1][j]
                else:
                    dp[i][j]+=dp[i+1][d-1]*dp[d-1][j]%MOD
                dp[i][j]%=MOD
print(dp[0][N-1])
