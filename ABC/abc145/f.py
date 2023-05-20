import collections
N,K=map(int, input().split())
array=list(map(int, input().split()))
INF=pow(10,11)
# dp[k][now]:=index iまででk回高さを変更したとき、現状now列塗っている最中での合計手数
dp=collections.defaultdict(lambda: collections.defaultdict(lambda: INF))
dp[0][0]=0
for i in range(N):
    #print(dp)
    nexts=collections.defaultdict(lambda: collections.defaultdict(lambda: INF))
    for k in dp:
        for now in dp[k]:
            v=dp[k][now]
            # 飛ばさない
            if now<=array[i]:
                nexts[k][array[i]]=min(nexts[k][array[i]],v+array[i]-now)
            else:
                nexts[k][array[i]]=min(nexts[k][array[i]],v)
            if k<K:
                # 飛ばす
                nexts[k+1][now]=min(nexts[k+1][now],v)
    dp=nexts
#print(dp)
ret=INF
for k in dp:
    for now in dp[k]:
        ret=min(ret,dp[k][now])
print(ret)
