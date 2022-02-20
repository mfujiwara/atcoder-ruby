import collections
N,M=map(int, input().split())
abs=[]
for i in range(M):
    a,b=map(int, input().split())
    abs.append((a-1,b-1))
array=list(map(int, input().split()))
rets=[""]*M
edges=collections.defaultdict(list)
targets=[]
for i,ab in enumerate(abs):
    a,b=ab
    if array[a]<array[b]:
        rets[i]="<-"
    elif array[a]>array[b]:
        rets[i]="->"
    else:
        targets.append((a,b,i))
        edges[a].append((b,i,True))
        edges[b].append((a,i,False))
while targets:
    a,b,i=targets.pop()
    if rets[i]!="":
        continue
    rets[i]="->"
    while edges[b]:
        c,i,orientation=edges[b].pop()
        if rets[i]!="":
            continue
        if orientation:
            rets[i]="->"
        else:
            rets[i]="<-"
        b=c
for ret in rets:
    print(ret)
