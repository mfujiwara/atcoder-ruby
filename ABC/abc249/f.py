import heapq
N,K=map(int, input().split())
ty=[(1,0)]
for _ in range(N):
    t,y=map(int, input().split())
    ty.append((t,y))
ret=-pow(10,20)
total=0
skip=0
pend=[]
while ty:
    t,y=ty.pop()
    if t==1:
        while skip>K and pend:
            total-=heapq.heappop(pend)
            skip-=1
        if skip>K:
            break
        ret=max(ret,total+y)
        skip+=1
    else:
        if y>=0:
            total+=y
        else:
            heapq.heappush(pend,-y)
            skip+=1
print(ret)
