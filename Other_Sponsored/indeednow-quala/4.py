H,W=map(int, input().split())
C=[list(map(int, input().split())) for _ in range(H)]
C=sum(C,[])
complete=[(i+1)%(H*W) for i in range(H*W)]
ret=0
done=set()
done.add(tuple(C))
targets=[C]
ret=0
while targets:
    nexts=[]
    for t in targets:
        if t==complete:
            print(ret)
            exit()
        i=t.index(0)
        r,c=divmod(i,W)
        if r>0:
            u=t[:]
            u[i],u[i-W]=u[i-W],u[i]
            tup=tuple(u)
            diff=0
            for j in range(H*W):
                if u[j]!=(j+1)%(H*W):
                    diff+=1
            if tup not in done and diff<25-ret:
                nexts.append(u)
                done.add(tup)
        if r<H-1:
            u=t[:]
            u[i],u[i+W]=u[i+W],u[i]
            tup=tuple(u)
            diff=0
            for j in range(H*W):
                if u[j]!=(j+1)%(H*W):
                    diff+=1
            if tup not in done and diff<25-ret:
                nexts.append(u)
                done.add(tup)
        if c>0:
            u=t[:]
            u[i],u[i-1]=u[i-1],u[i]
            tup=tuple(u)
            diff=0
            for j in range(H*W):
                if u[j]!=(j+1)%(H*W):
                    diff+=1
            if tup not in done and diff<25-ret:
                nexts.append(u)
                done.add(tup)
        if c<W-1:
            u=t[:]
            u[i],u[i+1]=u[i+1],u[i]
            tup=tuple(u)
            diff=0
            for j in range(H*W):
                if u[j]!=(j+1)%(H*W):
                    diff+=1
            if tup not in done and diff<25-ret:
                nexts.append(u)
                done.add(tup)
    targets=nexts
    ret+=1
