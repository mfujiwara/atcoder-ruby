import collections
N=int(input())
done=[False]*N
xy=[]
dots_x=collections.defaultdict(list)
dots_y=collections.defaultdict(list)
for i in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
    dots_x[x].append((i,y))
    dots_y[y].append((i,x))
ret=0
for i in range(N):
    if done[i]: continue
    done[i]=True
    c=1
    x,y=xy[i]
    xxx=set([x])
    yyy=set([y])
    targets=[i]
    while targets:
        t=targets.pop()
        x,y=xy[t]
        for u,uy in dots_x[x]:
            if done[u]: continue
            done[u]=True
            c+=1
            targets.append(u)
            yyy.add(uy)
        for u,ux in dots_y[y]:
            if done[u]: continue
            done[u]=True
            c+=1
            targets.append(u)
            xxx.add(ux)
    ret+=len(xxx)*len(yyy)-c
print(ret)
