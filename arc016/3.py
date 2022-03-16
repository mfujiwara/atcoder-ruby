import collections
N,M=map(int, input().split())
costs=[]
idols=[]
for _ in range(M):
    c,cost=map(int, input().split())
    costs.append(cost)
    dd=collections.defaultdict(int)
    for _ in range(c):
        idol,p=map(int, input().split())
        dd[idol-1]=p
    idols.append(dd)
INF=pow(10,10)
dp=[INF]*pow(2,N)
dp[0]=0
for bit in range(pow(2,N)):
    for i in range(M):
        y=100
        x=0
        for k,p in idols[i].items():
            if (bit>>k)&1==0:
                y -= p
            else:
                ns = bit^(1<<k)
                x+=p*dp[ns]
        if y > 0:
            dp[bit]=min(dp[bit], x/y+costs[i]*100/y)
print(dp[-1])
