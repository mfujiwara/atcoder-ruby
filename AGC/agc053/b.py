import heapq
N=int(input())
values=list(map(int, input().split()))
total=sum(values)
queue=[]
for i in range(N):
    heapq.heappush(queue,values[N+i])
    heapq.heappush(queue,values[N-1-i])
    v=heapq.heappop(queue)
    total-=v
print(total)
