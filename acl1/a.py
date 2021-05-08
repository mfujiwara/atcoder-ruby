N=int(input())
xyi=[]
for i in range(N):
    x,y=map(int, input().split())
    xyi.append((x,y,i))
xyi=sorted(xyi)
need_end=set()
stack=set()
counts=[0]
for x,y,i in xyi:
    counts[-1]+=1
    if N-x+1 in stack:
        stack.remove(N-x+1)
    else:
        need_end.add(N-x+1)
    if y in need_end:
        need_end.remove(y)
    else:
        stack.add(y)
    if len(need_end)==0:
        counts.append(0)
idx=0
rets=[-1]*N
for count in counts:
    for c in range(count):
        x,y,i=xyi[idx]
        rets[i]=count
        idx+=1
for r in rets:
    print(r)
