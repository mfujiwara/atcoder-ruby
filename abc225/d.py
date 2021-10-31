N,Q=map(int, input().split())
pre=[-1]*(N+1)
post=[-1]*(N+1)
for _ in range(Q):
    query=list(map(int, input().split()))
    if query[0]==1:
        x,y=query[1],query[2]
        post[x]=y
        pre[y]=x
    elif query[0]==2:
        x,y=query[1],query[2]
        post[x]=-1
        pre[y]=-1
    else:
        x=query[1]
        while pre[x]!=-1:
            x=pre[x]
        rets=[x]
        while post[x]!=-1:
            x=post[x]
            rets.append(x)
        print(len(rets),*rets)
