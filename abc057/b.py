N,M=map(int, input().split())
ab=[]
for _ in range(N):
    a,b=map(int, input().split())
    ab.append((a,b))
lc,ld=map(int, input().split())
cd=[]
for _ in range(M-1):
    c,d=map(int, input().split())
    cd.append((c,d))
for a,b in ab:
    ret=0
    v=abs(a-lc)+abs(b-ld)
    for i,c_d in enumerate(cd):
        c,d=c_d
        w=abs(a-c)+abs(b-d)
        if w<v:
            ret=i+1
            v=w
    print(ret+1)
