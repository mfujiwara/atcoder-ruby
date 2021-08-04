N,M=map(int, input().split())
edges=[set() for _ in range(N)]
for _ in range(M):
    a,b=map(int, input().split())
    a,b=a-1,b-1
    edges[a].add(b)
    edges[b].add(a)
rets1=["1"]
t=0
done=[False]*N
done[0]=True
while edges[t]:
    u=edges[t].pop()
    if done[u]:
        continue
    rets1.append(str(u+1))
    done[u]=True
    edges[u].remove(t)
    t=u
rets2=[]
t=0
while edges[t]:
    u=edges[t].pop()
    if done[u]:
        continue
    rets2.append(str(u+1))
    done[u]=True
    edges[u].remove(t)
    t=u
rets=rets2[::-1]+rets1
print(len(rets))
print(" ".join(rets))
