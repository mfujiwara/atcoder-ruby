import heapq
N,M=map(int, input().split())
xy=[]
for _ in range(N):
    x,y=map(int, input().split())
    xy.append((x,y))
xy.sort(reverse=True)
array=[]
for _ in range(M):
    a=int(input())
    array.append(a)
array.sort()
stack=[]
heapq.heapify(stack)
ret=0
for a in array:
    while len(xy)>0 and xy[-1][0]<=a:
        _,y=xy.pop()
        heapq.heappush(stack,y)
    while stack:
        y=heapq.heappop(stack)
        if a<=y:
            ret+=1
            break
print(ret)
