import sys
sys.setrecursionlimit(10**7)
N,Q=map(int, input().split())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    a,b,c,d=map(int, input().split())
    a-=1
    b-=1
    edges[a].append((b,c,d))
    edges[b].append((a,c,d))
queries=[[] for _ in range(N)]
for i in range(Q):
    x,y,u,v=map(int, input().split())
    u-=1
    v-=1
    queries[u].append((i,v,x,y))
    queries[v].append((i,u,x,y))
# p_edge[i]:=親への辺の色,距離 の組
p_edge=[None]*N
p_edge[0]=(0,0)
# parents[i]:=オイラーツアーで戻り済みの場合はiの親、Nより大きい時は戻ってない
parents=[N]*N
color_counts=[0]*N
color_dist=[0]*N
total_dist=0
targets=[(0,0)]
rets=[0]*Q
while targets:
    t,status=targets.pop()
    if status==0:
        targets.append((t,1))
        color_counts[p_edge[t][0]]+=1
        color_dist[p_edge[t][0]]+=p_edge[t][1]
        total_dist+=p_edge[t][1]
        for u,c,d in edges[t]:
            if p_edge[u]==None:
                p_edge[u]=(c,d)
                parents[u]=t+N
                targets.append((u,0))
    else:
        for i,u,x,y in queries[t]:
            ret=total_dist-color_dist[x]+y*color_counts[x]
            if u!=-1:
                rets[i]+=ret
                p=u
                while p!=0 and parents[p]<N:
                    p=parents[p]
                if p!=u:
                    parents[u]=p
                    queries[p].append((i,-1,x,y))
            else:
                rets[i]-=2*ret
        color_counts[p_edge[t][0]]-=1
        color_dist[p_edge[t][0]]-=p_edge[t][1]
        total_dist-=p_edge[t][1]
        parents[t]-=N
for ret in rets:
    print(ret)
