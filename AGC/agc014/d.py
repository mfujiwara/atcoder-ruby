N=int(input())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
parents=[-1]*N
targets=[0]
status=[0]*N
colors=[0]*N
parents=[-1]*N
while targets:
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                targets.append(u)
                parents[u]=t
    else:
        status[t]=2
        if colors[t]!=0:
            continue
        elif parents[t]==-1:
            if all([colors[u]==1 for u in edges[t]]):
                print("First")
                exit()
        elif colors[parents[t]]==0:
            colors[t]=-1
            colors[parents[t]]=1
        else:
            print("First")
            exit()
print("Second")
# print(parents)
# print(colors)
