N=int(input())
edges=[set() for _ in range(N)]
for i in range(N-1):
    p=int(input())
    edges[i+1].add(p)
    edges[p].add(i+1)
tours=[[] for _ in range(N)]
targets=[0]
c=0
while targets:
    t=targets.pop()
    tours[t].append(c)
    c+=1
    if c==(N-1)*2:
        break
    if edges[t]:
        for u in edges[t]:
            targets.append(t)
            edges[u].remove(t)
            targets.append(u)
        edges[t]=set()
for tour in tours:
    ret=0
    for i in range(len(tour)):
        a=tour[i]
        b=tour[(i+1)%len(tour)]
        if i+1==len(tour):
            b+=2*(N-1)
        r=(b-a)//2
        if r==0:
            r=N-1
        ret=max(ret,r)
    print(ret)
