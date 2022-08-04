MOD=pow(10,9)+7
n=int(input())
# 1で終わる長さiの列で最後の項以外が条件を満たすものの数
dp=[0,1,1,2]
sums=[0,1,2,4]
for i in range(4,n):
    dp.append((sums[-3]+dp[-1]+1)%MOD)
    sums.append((sums[-1]+dp[-1])%MOD)
# 全部同じ数, 最初が1以外の数でそれ以外が全部同じ数
ret=n+pow(n-1,2,MOD)
ret%=MOD
# 1以外の数の後に同じが続いて終わる
ret+=sums[n-2]*pow(n-1,2,MOD)%MOD
ret%=MOD
# 1の後に同じが続いて終わる
ret+=sums[n-1]*(n-1)%MOD
ret%=MOD
print(ret)
