import heapq
K=int(input())
N=int(input())
ad=[]
for _ in range(N):
    a,d=map(int, input().split())
    ad.append((a,d))
a,d=min(ad)
# 最終的な各値段が全て xx 以上
ok=0
ng=a+d*K+1
while ok+1<ng:
    mid=(ok+ng)//2
    must=0
    for a,d in ad:
        must+=max(0,mid-a+d-1)//d
    if must>K:
        ng=mid
    else:
        ok=mid
ret=0
for i in range(N):
    a,d=ad[i]
    c=(ok-a+d-1)//d
    if c>0:
        ret+=(a+a+d*(c-1))*c//2
        K-=c
        ad[i]=(a+d*c,d)
heapq.heapify(ad)
while K>0:
    a,d=heapq.heappop(ad)
    ret+=a
    K-=1
    heapq.heappush(ad,(a+d,d))
print(ret)
