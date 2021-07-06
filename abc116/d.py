import collections
import heapq
N,K=map(int, input().split())
sushi=[]
for _ in range(N):
    t,d=map(int, input().split())
    sushi.append((t,d))
sushi.sort(key=lambda e: (-e[1],e[0]))
base=0
queue=[]
counts=collections.defaultdict(int)
for i in range(K):
    t,d=sushi[i]
    base+=d
    if counts[t]!=0:
        queue.append(d)
    counts[t]+=1
heapq.heapify(queue)
ret=base+pow(len(counts),2)

for i in range(K,N):
    if len(queue)==0: break
    t,d=sushi[i]
    if counts[t]>0:
        continue
    exclude_d=heapq.heappop(queue)
    base-=exclude_d
    base+=d
    counts[t]+=1
    new_ret=base+pow(len(counts),2)
    ret=max(ret,new_ret)
print(ret)
