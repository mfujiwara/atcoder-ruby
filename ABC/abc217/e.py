import collections
import heapq
Q=int(input())
array=[]
tail=collections.deque([])
heapq.heapify(array)
for _ in range(Q):
    q=input()
    if q=="2":
        if array:
            print(heapq.heappop(array))
        else:
            print(tail.popleft())
    elif q=="3":
        while tail:
            heapq.heappush(array,tail.pop())
    else:
        _,x=map(int, q.split())
        tail.append(x)
