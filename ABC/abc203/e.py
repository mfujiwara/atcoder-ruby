N,M=map(int, input().split())
xys=[]
for _ in range(M):
    x,y=map(int, input().split())
    xys.append((x,y))
xys.sort()
maps={}
pressed=[]
v=0
for x,y in xys:
    if x in maps:
        pressed[maps[x]].add(y)
    else:
        pressed.append(set([y]))
        maps[x]=v
        v+=1
targets=set([N])
for y_set in pressed:
    removes=set()
    adds=set()
    for y in y_set:
        removes.add(y)
        if y-1 in targets or y+1 in targets:
            adds.add(y)
    for r in removes:
        if r in targets:
            targets.remove(r)
    for a in adds:
        targets.add(a)
print(len(targets))
