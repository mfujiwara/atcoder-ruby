MOD=998244353
N,D=map(int, input().split())
p_array=list(map(int, input().split()))
q_array=list(map(int, input().split()))

# dp[i][j]:=pとの距離がi,qとの距離がjである点の数
dp=[[0]*(D+1) for _ in range(D+1)]
dp[0][0] = 1
for i in range(N):
    nexts=[[0]*(D+1) for _ in range(D+1)]
    p=p_array[i]
    q=q_array[i]
    d=abs(p-q)
    # pとqの間
    tmp=[[0]*(D+1) for _ in range(D+1)]
    for i in range(D+1):
        for j in range(D+1):
            tmp[i][j]=dp[i][j]
            if i != 0 and j != D:
                tmp[i][j]+=tmp[i-1][j+1]
                tmp[i][j]%=MOD
    for i in range(D+1):
        for j in range(D+1):
            si=i
            sj=j-d
            if sj<0:
                si+=sj
                sj=0
            if 0<=si<=D and 0<=sj<= D:
                nexts[i][j]+=tmp[si][sj]
                nexts[i][j]%=MOD
            ti=i-(d+1)
            tj=j+1
            if 0<=ti<=D and 0<=tj<=D:
                nexts[i][j]-=tmp[ti][tj]
                nexts[i][j]%=MOD
    # pとqの間以外
    tmp=[[0]*(D+1) for _ in range(D+1)]
    for i in range(D+1):
        for j in range(D+1):
            tmp[i][j]=dp[i][j]
            if i != 0 and j != 0:
                tmp[i][j]+=tmp[i-1][j-1]
                tmp[i][j]%=MOD
    for i in range(D+1):
        for j in range(D+1):
            if i+1<=D and j+d+1<=D:
                nexts[i+1][j+d+1]+=tmp[i][j]
                nexts[i+1][j+d+1]%=MOD
            if i+d+1<=D and j+1<=D:
                nexts[i+d+1][j+1]+=tmp[i][j]
                nexts[i+d+1][j+1]%=MOD
    dp=nexts
ret=0
for i in range(D+1):
    for j in range(D+1):
        ret+=dp[i][j]
        ret%=MOD
print(ret)
