N=int(input())
tlr=[]
for _ in range(N):
    t,l,r=map(int, input().split())
    if t==2 or t==4:
        r-=0.1
    if t==3 or t==4:
        l+=0.1
    tlr.append((t,l,r))
ret=0
for i in range(N-1):
    t1,l1,r1=tlr[i]
    for j in range(i+1,N):
        t2,l2,r2=tlr[j]
        if (l1<=l2 and l2<=r1) or (l2<=l1 and l1<=r2):
            ret+=1
print(ret)
