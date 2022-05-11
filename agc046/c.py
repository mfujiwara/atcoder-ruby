import collections
MOD=998244353
S,K=input().split()
K=int(K)
counts=[0,0]
total=0
for ch in S[::-1]:
    if ch=="0":
        counts.append(0)
    else:
        counts[-1]+=1
        total+=1
# dp[i][j][k]:=index iまででk回の移動とj個の場所確定させた場合の数
dp=[collections.defaultdict(int) for _ in range(total+1)]
dp[0][0]=1
sub_total=0
for i in range(1,len(counts)):
    nexts=[collections.defaultdict(int) for _ in range(total+1)]
    sub_total+=counts[i]
    for j in range(sub_total+1):
        for j0 in range(j+1):
            for k0 in dp[j0]:
                k=k0+max(0,counts[i]-(j-j0))
                if k<=K:
                    nexts[j][k]+=dp[j0][k0]
                    nexts[j][k]%=MOD
    dp=nexts
print(sum(dp[-1].values())%MOD)
