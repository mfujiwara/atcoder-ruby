import collections
M=int(input())
edges=collections.defaultdict(list)
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
array=list(map(int, input().split()))
mmm=[8]*9
for i in range(8):
    array[i]-=1
    mmm[array[i]]=i
memo={}
memo[tuple(mmm)]=0
targets=[mmm]
while targets:
    nexts=[]
    for t in targets:
        if all([t[i]==i for i in range(8)]):
            print(memo[tuple(t)])
            exit()
        space=t.index(8)
        for u in edges[space]:
            tt=t[:]
            tt[space],tt[u]=tt[u],tt[space]
            if tuple(tt) in memo: continue
            memo[tuple(tt)]=memo[tuple(t)]+1
            nexts.append(tt)
    targets=nexts
print(-1)
