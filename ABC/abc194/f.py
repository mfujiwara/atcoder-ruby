import collections
MOD=10**9+7
N,K=input().split()
K=int(K)
# dp0[i]:=Nと同じでbitの立っている数を使っている場合の数
dp0=collections.defaultdict(int)
# dp1[i]:=Nより小さいのが確定していてi種類使っている場合の数
dp=[0]*17
done=set()
for i in range(len(N)):
    d=int(N[i]) if N[i] in "0123456789" else ord(N[i])-ord("A")+10
    #print("d",d)
    nexts=[0]*17
    if len(done)<=K:
        for j in range(d):
            if j in done:
                nexts[len(done)]+=1
            elif len(done)<K:
                if i!=0 or j!=0:
                    nexts[len(done)+1]+=1
    if i!=0:
        nexts[1]+=15
    #print("1",nexts)
    for k in range(1,K+1):
        nexts[k]+=dp[k]*k
        #print("1.1",nexts,dp[k])
        nexts[k]+=dp[k-1]*(16-k+1)
        #print("1.2",nexts,dp[k-1])
        nexts[k]%=MOD
    dp=nexts
    done.add(d)
    #print("2",nexts)
ret=dp[K]
if len(done)==K:
    ret+=1
    ret%=MOD
print(ret)
