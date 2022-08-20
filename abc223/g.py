N=int(input())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
# dp[i]:=点iについて、配下のペア数と直下の余白数の組(余白数が0の場合、削除されてもいい)
dp=[None]*N
targets=[(0,0)]
parents=[-2]*N
parents[0]=-1
while targets:
    t,status=targets.pop()
    if status==0:
        targets.append((t,1))
        for u in edges[t]:
            if parents[u]==-2:
                parents[u]=t
                targets.append((u,0))
    else:
        count=0
        blank=0
        for u in edges[t]:
            if parents[t]!=u:
                uc,ub=dp[u]
                count+=uc
                if ub==0:
                    blank+=1
        if blank>0:
            count+=1
        dp[t]=(count,blank)
#print(dp)
targets=[0]
# dp1[i]:=点iについて親側を調べた時に、親とペアを組むことになるかどうか
dp1=[False]*N
while targets:
    t=targets.pop()
    for u in edges[t]:
        if parents[t]!=u:
            targets.append(u)
            if dp1[t]:
                continue
            else:
                v=1 if dp[u][1]==0 else 0
                if dp[t][1]-v==0:
                    dp1[u]=True
#print(dp1)
ret=0
for i in range(N):
    if dp[i][1]==0 and not dp1[i]:
        ret+=1
print(ret)
