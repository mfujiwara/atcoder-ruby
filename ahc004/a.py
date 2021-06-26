import collections
import heapq
N,M=map(int, input().split())
rets=[""]
sss=[]
heapq.heapify(sss)
for _ in range(M):
    s=input()
    heapq.heappush(sss,(len(s),s))
t_score=collections.defaultdict(int)
ttt=[]
heapq.heapify(ttt)
while sss:
    _,s=heapq.heappop(sss)
    score=0
    for t in t_score:
        if s.count(t) > 0:
            score+=t_score[t]
    t_score[s]=score+1
    heapq.heappush(ttt,(-score,s))
#print(t_score)
sss=ttt
while sss:
    _,s=heapq.heappop(sss)
    #print(f"s: {s}")
    done=False
    for r in rets:
        if r.count(s)>0:
            done=True
            break
    if done:
        continue
    for i in range(len(rets)):
        if len(rets[i])+len(s)<=N:
            rets[i]+=s
            done=True
            break
    if done:
        continue
    rets.append(s)
for i in range(len(rets)):
    if len(rets[i])<N:
        rets[i]+="."*(N-len(rets[i]))
while len(rets)<N:
    rets.append("."*N)
for i in range(N):
    print(rets[i])
