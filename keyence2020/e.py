import collections


N,M=map(int, input().split())
array=list(map(int, input().split()))
sorted_array=sorted([(a,i) for i,a in enumerate(array)])
edges=[]
shortest=[(array[i],N) for i in range(N)]
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges.append((u,v))
    shortest[u]=min(shortest[u],(array[v],v))
    shortest[v]=min(shortest[v],(array[u],u))
shortest_edges=collections.defaultdict(list)
for i,(c,p) in enumerate(shortest):
    shortest_edges[i].append((p,c))
    shortest_edges[p].append((i,c))
colors=[None]*N
ddd={}
#print(sorted_array)
for a,i in sorted_array:
    pa,p=shortest[i]
    if p==N:
        print(-1)
        exit()
    if colors[i]==None:
        colors[i]=1
    targets=[i]
    while targets:
        t=targets.pop()
        for u,c in shortest_edges[t]:
            if colors[u]==None:
                colors[u]=-colors[t]
                targets.append(u)
                maxi=max(array[t],array[u])
                ddd[(t,u)]=maxi
                ddd[(u,t)]=maxi
for c in colors:
    if c==1:
        print("B",end="")
    else:
        print("W",end="")
print()
for u,v in edges:
    if (u,v) in ddd:
        print(ddd[(u,v)])
    else:
        print(pow(10,9))
