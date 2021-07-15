import bisect
N=int(input())
his=[]
for i in range(N):
    h=int(input())
    his.append((h,i))
his.sort()
done=[-1,N]
rets=[0]*N
while his:
    h,i=his.pop()
    indexes=[i]
    while his and his[-1][0]==h:
        _,i=his.pop()
        indexes.append(i)
    j_indexes=[]
    for i in indexes:
        j=bisect.bisect(done,i)
        j_indexes.append(j)
        rets[i]=done[j]-done[j-1]-2
    for i in indexes:
        bisect.insort(done, i)
for r in rets:
    print(r)
