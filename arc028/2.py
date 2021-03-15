import heapq
N,K=map(int, input().split())
array=list(map(int, input().split()))
youngers=[]
olders=[]
for i in range(K-1):
    x=array[i]
    youngers.append((-x,i)) # -age_idx, score_idx
heapq.heapify(youngers)
heapq.heapify(olders)
for i in range(K-1,N):
    x=array[i]
    heapq.heappush(youngers,(-x,i))
    y,i=heapq.heappop(youngers)
    heapq.heappush(olders,(-y,i))
    _,idx=olders[0]
    print(idx+1)
