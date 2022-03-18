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
dp=[INF]*pow(2,N) # その状態から全部揃えるのにかかる金額の期待値
dp[-1]=0
for bit in range(pow(2,N)-2,-1,-1):
    for i in range(M):
        x=0 # 遷移後の期待値の合計
        y=0 # 他の状態に遷移する確率
        for k,p in idols[i].items():
            if bit&(1<<k)==0:
                x+=p*dp[bit|(1<<k)]
                y+=p
        if y>0:
            # 遷移後のコストの期待値 + 他の状態に遷移するのにかかるコストの期待値
            dp[bit]=min(dp[bit],x/y+costs[i]*100/y)
print(dp[0])
