import collections
MOD=998244353
N=int(input())
S="_"+input()
dp=[collections.defaultdict(int) for _ in range(N+1)]
for i in range(1,len(S)):
    c=ord(S[i])-ord("A")
    bit=1<<c
    dp[i][(c,bit)]+=1
    for key in dp[i-1]:
        last,bits=key
        if last==c or bits&bit==0:
            dp[i][(c,bits|bit)]=(dp[i][(c,bits|bit)]+dp[i-1][key])%MOD
        dp[i][key]+=dp[i-1][key]
ret=0
for key in dp[-1]:
    ret+=dp[-1][key]
    ret%=MOD
print(ret)
