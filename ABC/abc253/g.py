N,L,R=map(int, input().split())
def calc(n):
    i=N
    s=0
    while n>=i:
        n-=i-1
        i-=1
        s+=1
    t=s+n
    return (s,t)
l1,l2=calc(L)
r1,r2=calc(R)
#print(l1,l2,r1,r2)
if l1==r1:
    rets=[i+1 for i in range(N)]
    for i in range(l2,r2+1):
        rets[l1],rets[i]=rets[i],rets[l1]
    print(*rets)
else:
    rets=[i+1 for i in range(N)]
    for i in range(l2,N):
        rets[l1],rets[i]=rets[i],rets[l1]
    #print(rets)
    if l1+1<r1:
        d=r1-l1-1
        rets=rets[:l1+1]+rets[-d:][::-1]+rets[l1+1:-d]
    #print(rets)
    for i in range(r1+1,r2+1):
        rets[r1],rets[i]=rets[i],rets[r1]
    #print(rets)
    print(*rets)
