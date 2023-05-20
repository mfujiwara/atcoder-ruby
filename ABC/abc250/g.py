import heapq
N=int(input())
array=list(map(int, input().split()))
ret=0
queue=[]
for a in array:
    if queue and queue[0]<a:
        ret+=a-queue[0]
        heapq.heappop(queue)
        heapq.heappush(queue,a)
        heapq.heappush(queue,a)
    else:
        heapq.heappush(queue,a)
print(ret)
