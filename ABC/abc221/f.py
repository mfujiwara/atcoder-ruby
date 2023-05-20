import collections
MOD=998244353
N=int(input())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
targets=[0]
done=[False]*N
done[0]=True
while targets:
    nexts=[]
    for t in targets:
        for u in edges[t]:
            if done[u]: continue
            nexts.append(u)
            done[u]=True
    if len(nexts)==0:
        break
    targets=nexts
targets=targets[:1]
done=[None]*N
done[targets[0]]=(0,-1)
while targets:
    nexts=[]
    for t in targets:
        for u in edges[t]:
            if done[u]!=None: continue
            nexts.append(u)
            done[u]=(done[t][0]+1,t)
    if len(nexts)==0:
        break
    targets=nexts
D=done[targets[0]][0]
if D%2==0:
    t=targets[0]
    for _ in range(D//2):
        t=done[t][1]
    targets=edges[t]
    done=[None]*N
    done[t]=(0,-1)
    for u in targets:
        done[u]=(1,u)
    dd=D//2
else:
    t=targets[0]
    for _ in range(D//2):
        t=done[t][1]
    targets=[t,done[t][1]]
    done=[None]*N
    for u in targets:
        done[u]=(0,u)
    dd=D//2
groups=collections.defaultdict(int)
while targets:
    t=targets.pop()
    if done[t][0]==dd:
        groups[done[t][1]]+=1
    for u in edges[t]:
        if done[u]!=None: continue
        done[u]=(done[t][0]+1,done[t][1])
        targets.append(u)
ret=1
for v in groups.values():
    ret*=(v+1)
    ret%=MOD
ret-=(sum(groups.values())+1)
ret+=MOD
ret%=MOD
print(ret)
