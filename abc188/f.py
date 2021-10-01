X,Y=map(int, input().split())
if X>=Y:
    print(X-Y)
    exit()
ret=Y-X
targets=[Y]
c=0
done=set()
while targets and ret>c:
    nexts=[]
    for t in targets:
        if t<=X:
            ret=min(ret,c+X-t)
            continue
        ret=min(ret,c+t-X)
        if t%2==0:
            u=t//2
            if u not in done:
                nexts.append(u)
                done.add(u)
        else:
            u=t+1
            if u not in done:
                nexts.append(u)
                done.add(u)
            u=t-1
            if u not in done:
                nexts.append(u)
                done.add(u)
    targets=nexts
    c+=1
print(ret)

