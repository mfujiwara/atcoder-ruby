import collections
MOD=pow(10,9)+7
N=int(input())
S=input()
if S[0]=="W":
    print(0)
    exit()
dp=[collections.defaultdict(int) for _ in range(2*N)]
dp[0][(1,True)]=1
for i,ch in enumerate(S):
    if i==0: continue
    same_pre=(ch==S[i-1])
    for key in dp[i-1]:
        pre_v=dp[i-1][key]
        open_count,is_open=key
        if open_count<0 or open_count>2*N-i: continue
        if is_open:
            if same_pre:
                dp[i][(open_count-1,False)]+=pre_v*open_count%MOD
                dp[i][(open_count-1,False)]%=MOD
            else:
                dp[i][(open_count+1,True)]+=pre_v
                dp[i][(open_count+1,True)]%=MOD
        else:
            if same_pre:
                dp[i][(open_count+1,True)]+=pre_v
                dp[i][(open_count+1,True)]%=MOD
            else:
                dp[i][(open_count-1,False)]+=pre_v*open_count%MOD
                dp[i][(open_count-1,False)]%=MOD
ret=dp[-1][(0,False)]
for i in range(2,N+1):
    ret*=i
    ret%=MOD
print(ret)
