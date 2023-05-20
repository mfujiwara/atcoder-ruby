import collections
N=int(input())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
def calc(s):
    ddd=[-1]*N
    ddd[s]=0
    targets=[s]
    while targets:
        t=targets.pop()
        for u in edges[t]:
            if ddd[u]==-1:
                ddd[u]=ddd[t]+1
                targets.append(u)
    ret_d=0
    ret_i=s
    for i,d in enumerate(ddd):
        if d>ret_d:
            ret_d=d
            ret_i=i
    return (ret_d,ret_i)
_,t0=calc(0)
_,t1=calc(t0)
#print((t0,t1))
Q=int(input())
queries=[[] for _ in range(N)]
for i in range(Q):
    u,k=map(int, input().split())
    u-=1
    queries[u].append((i,k))
#print(queries)
rets=[-1]*Q
targets=[t0]
status=[0]*N
path=[]
while targets:
    #print(t0,path)
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        tmp=[]
        for index,k in queries[t]:
            if len(path)>=k:
                rets[index]=path[-k]+1
            else:
                tmp.append((index,k))
        queries[t]=tmp
        path.append(t)
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                targets.append(u)
    else:
        path.pop()
targets=[t1]
status=[0]*N
path=[]
while targets:
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        tmp=[]
        for index,k in queries[t]:
            if len(path)>=k:
                rets[index]=path[-k]+1
            else:
                tmp.append((index,k))
        queries[t]=tmp
        path.append(t)
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                targets.append(u)
    else:
        path.pop()
print(*rets,sep="\n")
