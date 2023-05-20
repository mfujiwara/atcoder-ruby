import collections
N,K=map(int, input().split())
edges=collections.defaultdict(list)
for _ in range(N-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
parents=[-1]*N
leaf_to_root=[]
targets=[0]
while targets:
    t=targets.pop()
    leaf_to_root.append(t)
    for u in edges[t]:
        if parents[t]==u: continue
        parents[u]=t
        targets.append(u)
leaf_to_root=leaf_to_root[::-1]
#print(parents,leaf_to_root)
def calc(n):
    total=0
    # dp[i]:=特別な点は-n,ギリギリ届くのが0,届かないのが正の数,n+1は特別な点にする必要がある
    dp=[None]*N
    for t in leaf_to_root:
        if t!=0 and len(edges[t])==1:
            dp[t]=1
            continue
        mini=n+1
        maxi=-n
        for u in edges[t]:
            if parents[t]==u: continue
            mini=min(mini,dp[u]+1)
            maxi=max(maxi,dp[u]+1)
        if mini+maxi<=1:
            # 届く
            dp[t]=mini
        elif maxi==n+1:
            # 特別な点
            dp[t]=-n
            total+=1
        else:
            # 届かない
            dp[t]=maxi
    if dp[0]>0:
        total+=1
    #print(n,total,dp)
    return total<=K
ng=0
ok=2*pow(10,5)
while ng+1<ok:
    mid=(ng+ok)//2
    if calc(mid):
        ok=mid
    else:
        ng=mid
print(ok)
