import heapq
N=int(input())
array=list(map(int, input().split()))
for i in range(N):
    array[i]*=-1
heapq.heapify(array)
ret=0
while array[0]<=-N:
    a=heapq.heappop(array)
    r,q=divmod(-a,N)
    ret+=r
    for i in range(len(array)):
        array[i]-=r
    heapq.heappush(array,-q)
print(ret)
