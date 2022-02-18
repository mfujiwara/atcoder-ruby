MOD=998244353
N,K=map(int, input().split())
p_array=list(map(int, input().split()))
q_array=list(map(int, input().split()))
array=[-1]*N
for i in range(N):
    array[p_array[i]-1]=q_array[i]-1
dp=[[0]*(N+1) for _ in range(K+1)] # dp[j][k]:=j人まで選んで、選ばなかった中で最高の順位がkの場合の数
dp[0][N]=1
for i in range(N): # 1回目のテストがいい順番に選ぶ/選ばないを決める
    nexts=[[0]*(N+1) for _ in range(K+1)]
    for j in range(K+1):
        for k in range(N+1):
            if j<K and array[i]<k:
                # i番目の人が k よりいい順位なら選ぶことができる（kより悪かったら条件不一致）
                nexts[j+1][k]+=dp[j][k]
                nexts[j+1][k]%=MOD
            # i番目の人を選ばない
            nexts[j][min(k,array[i])]+=dp[j][k]
            nexts[j][min(k,array[i])]%=MOD
    dp=nexts
print(sum(dp[-1])%MOD)
