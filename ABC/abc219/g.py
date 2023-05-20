N,M,Q=map(int, input().split())
edges=[set() for _ in range(N)]
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].add(v)
    edges[v].add(u)
B=int(M**0.5)
b_edges=[set() for _ in range(N)]
for u in range(N):
    for v in edges[u]:
        if len(edges[v])>=B:
            b_edges[u].add(v)
array=list(map(int, input().split()))
# 世代と値の組み
values=[(-1,i+1) for i in range(N)]
flags=[None]*N
for i,x in enumerate(array):
    x-=1
    g,v=values[x]
    # xの値を最新に更新
    for z in b_edges[x]:
        if flags[z] and flags[z][0]>g:
            g,v=flags[z]
    values[x]=(i,v)
    if len(edges[x])>=B:
        # 印だけつける
        flags[x]=(i,v)
    else:
        # 実際に更新
        for y in edges[x]:
            values[y]=(i,v)
    #print(values,flags)
rets=[]
for x in range(N):
    g,v=values[x]
    for z in b_edges[x]:
        if flags[z] and flags[z][0]>g:
            g,v=flags[z]
    rets.append(v)
print(*rets)
