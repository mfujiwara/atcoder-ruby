import collections
N,M=map(int, input().split())
edges=collections.defaultdict(list)
reverse=collections.defaultdict(list)
array=[]
for _ in range(M):
    s,t=map(int, input().split())
    s,t=s-1,t-1
    edges[s].append(t)
    reverse[t].append(s)
    array.append((s,t))
targets=[[0]]
done=[False]*N
done[0]=True
shortest=[]
while targets:
    nexts=[]
    for t in targets:
        for u in edges[t[-1]]:
            if done[u]:
                continue
            done[u]=True
            tt=t[:]
            tt.append(u)
            if u==N-1:
                shortest=tt
                break
            nexts.append(tt)
    targets=nexts
paths=set()
for i in range(len(shortest)-1):
    paths.add((shortest[i],shortest[i+1]))
for ss,tt in array:
    if len(paths)==0:
        print(-1)
        continue
    if (ss,tt) not in paths:
        print(len(paths))
        continue
    targets=[0]
    done=[False]*N
    done[0]=True
    ret=1
    while targets:
        nexts=[]
        for t in targets:
            for u in edges[t]:
                if done[u] or (t,u)==(ss,tt):
                    continue
                done[u]=True
                if u==N-1:
                    break
                nexts.append(u)
        if done[-1]:
            break
        targets=nexts
        ret+=1
    if done[-1]:
        print(ret)
    else:
        print(-1)
