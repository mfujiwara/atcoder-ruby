N,M=map(int, input().split())
edges=[[] for _ in range(N)]
for _ in range(M):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
state=[0]*N
c0=c1=c2=0
for i in range(N):
    if state[i]!=0: continue
    if len(edges[i])==0:
        c0+=1
        continue
    b=True
    state[i]=1
    targets=[i]
    while targets:
        t=targets.pop()
        for u in edges[t]:
            if state[u]==0:
                state[u]=-state[t]
                targets.append(u)
            else:
                if state[u]==state[t]:
                    b=False
    if b:
        c1+=1
    else:
        c2+=1
ret=c0*c0+2*c0*(N-c0)+2*c1*c2+2*c1*c1+c2*c2
print(ret)
#print(c0,c1,c2)
