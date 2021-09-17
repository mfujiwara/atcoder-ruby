import collections
BASE=ord("a")
N,K=map(int, input().split())
S=input()
targets=set()
queue=collections.deque([])
dajare=collections.deque([])
dajare_count=[0]*26
for i in range(K):
    v=ord(S[i])-BASE
    dajare.append(v)
    dajare_count[v]+=1
    queue.append(tuple([]))
queue.popleft()
queue.append(tuple(dajare_count))
for i in range(K,N):
    targets.add(queue.popleft())
    v=dajare.popleft()
    dajare_count[v]-=1
    v=ord(S[i])-BASE
    dajare.append(v)
    dajare_count[v]+=1
    t=tuple(dajare_count)
    if t in targets:
        print("YES")
        exit()
    queue.append(t)
print("NO")
