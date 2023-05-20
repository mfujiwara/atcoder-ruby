import collections
from sys import path_importer_cache
INF=1<<30
N,M=map(int, input().split())
dict=collections.defaultdict(list)
for i in range(M):
    a,b=map(int, input().split())
    dict[a-1].append(b-1)
    dict[b-1].append(a-1)
K=int(input())
c_array=list(map(int, input().split()))
dist=[[INF]*N for _ in range(K)]
for i in range(K):
    c_array[i]-=1
    targets=[c_array[i]]
    c=0
    while targets:
        tmp=[]
        for t in targets:
            if dist[i][t]==INF:
                dist[i][t]=c
                tmp+=dict[t]
        c+=1
        targets=tmp
# 巡回セールスマン
for i,ci in enumerate(c_array):
    for j,cj in enumerate(c_array):
        if dist[i][cj]==INF:
            print(-1)
            exit()
dp=[[0]*K if i==0 else [INF]*K for i in range(2**K)] # dp[set][end node]
for bit in range(1,2**K):
    # bitが表す集合を全て含みiが終端になるような経路のコストを求める
    for i in range(K):
        if not bit & (1<<i):
            continue
        pre_bit = bit ^ (1<<i)
        if pre_bit==0:
            dp[bit][i]=1
            continue
        for j in range(K):
            if dp[pre_bit][j]==INF:
                continue
            dp[bit][i]=min(
                dp[bit][i],
                dp[pre_bit][j]+dist[i][c_array[j]]
            )
print(min(dp[-1]))
