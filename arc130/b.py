H,W,C,Q=map(int, input().split())
tnc=[]
for _ in range(Q):
    t,n,c=map(int, input().split())
    tnc.append((t,n-1,c-1))
h=H
w=W
colored_h=set()
colored_w=set()
rets=[0]*C
while tnc:
    t,n,c=tnc.pop()
    if t==1 and n not in colored_h:
        rets[c]+=w
        colored_h.add(n)
        h-=1
    elif t==2 and n not in colored_w:
        rets[c]+=h
        colored_w.add(n)
        w-=1
print(*rets)
