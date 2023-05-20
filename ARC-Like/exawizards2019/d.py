import collections
MOD=pow(10,9)+7
N,X=map(int, input().split())
array=list(map(int, input().split()))
array.sort(reverse=True)
fn=[1,1]
inv=[1,1]
fn_inv=[1,1]
for n in range(2,N):
    fn.append(fn[-1]*n%MOD)
    inv.append(MOD - inv[MOD % n] * (MOD // n) % MOD)
    fn_inv.append(fn_inv[-1]*inv[-1]%MOD)
dp=[collections.defaultdict(int) for _ in range(N)] # dp[i]:=array[i]までを使った時の(途中の値 to 場合の数)の辞書
for i,a in enumerate(array):
    # i個のSをN-1個のうちから選べる
    v=fn[N-1]*fn_inv[N-1-i]%MOD
    dp[i][X%a]+=v
    if i>0:
        for key in dp[i-1]:
            dp[i][key%a]+=dp[i-1][key]
    for j in range(i-1):
        # i-j-2個のSをN-j-2のうちから選べる
        v0=fn[N-j-2]*fn_inv[N-i-1]%MOD
        for key in dp[j]:
            v=v0*dp[j][key]%MOD
            new_key=key%a
            dp[i][new_key]+=v
            dp[i][new_key]%=MOD
ret=0
for key in dp[-1]:
    c=dp[-1][key]
    ret+=c*key%MOD
    ret%=MOD
print(ret)
