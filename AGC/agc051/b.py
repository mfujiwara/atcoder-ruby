print(729)
l=[0,1,4,13,40,121,364]
targets=[(6,0,364)] # (d,x,y)
while targets:
    d,x,y=targets.pop()
    if d==0:
        print(x,y)
    else:
        m=l[d-1]*2+1
        targets.append((d-1,x,y))
        targets.append((d-1,x+m,y))
        targets.append((d-1,x,y-m))
