N,M=map(int, input().split())
edges=[set() for _ in range(N)]
for _ in range(M):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].add(b)
    edges[b].add(a)
for i in range(N):
    if len(edges[i])%2==1:
        print("No")
        exit()
ns=set(range(N))
loops=[]
while ns:
    now=ns.pop()
    ns.add(now)
    loop=[-1,now]
    indexes={}
    indexes[now]=1
    while True:
        #print(edges,now)
        nx=edges[now].pop()
        if nx==loop[-2]:
            nx1=edges[now].pop()
            edges[now].add(nx1)
            edges[now].add(nx)
            nx=nx1
        else:
            edges[now].add(nx)
        if nx in indexes:
            loop.append(nx)
            for i in range(indexes[nx],len(loop)-1):
                a=loop[i]
                b=loop[i+1]
                edges[a].remove(b)
                if len(edges[a])==0:
                    ns.remove(a)
                edges[b].remove(a)
                if len(edges[b])==0:
                    ns.remove(b)
            loops.append(loop[indexes[nx]:])
            break
        else:
            indexes[nx]=len(loop)
            loop.append(nx)
            now=nx
if len(loops)>=3:
    print("Yes")
elif len(loops)==2 and len(set(loops[0])&set(loops[1]))>=3:
    print("Yes")
else:
    print("No")
