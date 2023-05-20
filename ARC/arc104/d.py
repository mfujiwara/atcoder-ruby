import collections
N,K,M=map(int,input().split())
maxi=N*N*K+10
# dp[i][j]:=0..iまでの数をK個以内で合計がjになるものの数
dp=[]
counts=[0]*maxi
counts[0]=1
dp.append(counts)
for n in range(1,N+1):
    counts=dp[-1][:]
    # nで割った集合ごとに考える
    for i in range(n):
        tmp=0
        for k in range(i,maxi,n):
            tmp+=dp[-1][k]
            if k>=n*(K+1):
                # K個で届かないので引く
                tmp-=dp[-1][k-n*(K+1)]
            tmp%=M
            counts[k]=tmp
    dp.append(counts)
#print(dp)
for x in range(1,N+1):
    # 平均xになるものをカウント
    ret=0
    for j in range(maxi):
        # xより小さい大きいに分けた時に釣り合う場合の数
        ret+=dp[x-1][j]*dp[N-x][j]
        ret%=M
    ret*=(K+1) # xが0..K個の場合
    print((ret-1)%M) # 0x0の場合を引く
