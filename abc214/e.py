import collections
import heapq
T=int(input())
for _ in range(T):
    N=int(input())
    lr=collections.defaultdict(list)
    l_keys=set()
    for i in range(N):
        l,r=map(int, input().split())
        lr[l].append(r)
        l_keys.add(l)
    l_keys=sorted(list(l_keys))
    l_keys.append(pow(10,9)+1)
    valid=True
    balls=[]
    heapq.heapify(balls)
    for i,l in enumerate(l_keys):
        for r in lr[l]:
            heapq.heappush(balls,r)
        while balls:
            if i+1<len(l_keys) and l==l_keys[i+1]:
                break
            r=heapq.heappop(balls)
            if l>r:
                valid=False
                break
            l+=1
        if not valid:
            break
    if valid:
        print("Yes")
    else:
        print("No")
