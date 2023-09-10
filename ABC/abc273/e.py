Q=int(input())
note={}
queries=[]
children=[[] for _ in range(Q)]
roots=set([0])
for i in range(Q):
    query=input()
    if query=="DELETE":
        queries.append(("D",-1))
        if i>0:
            children[i-1].append(i)
    else:
        query,x=query.split()
        x=int(x)
        if query=="ADD":
            queries.append(("A",x))
            if i>0:
                children[i-1].append(i)
        elif query=="SAVE":
            queries.append(("S",x))
            note[x]=i
            if i>0:
                children[i-1].append(i)
        else:
            queries.append(("L",x))
            if x in note:
                children[note[x]].append(i)
            else:
                roots.add(i)
rets=[-1]*Q
for i in roots:
    array=[]
    targets=[(i,0)]
    while targets:
        t,s=targets.pop()
        if s==0:
            query,x=queries[t]
            if query=="D":
                if array:
                    x=array.pop()
                    queries[t]=("D",x)
            elif query=="A":
                array.append(x)
            if array:
                rets[t]=array[-1]

            targets.append((t,1))
            for c in children[t]:
                targets.append((c,0))
        else:
            query,x=queries[t]
            if query=="D":
                if x>0:
                    array.append(x)
            elif query=="A":
                array.pop()
print(*rets)
