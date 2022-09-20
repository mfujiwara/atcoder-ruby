import heapq
INF=pow(10,10)
W,H,Q=map(int, input().split())
www=[[] for _ in range(pow(10,5))]
hhh=[[] for _ in range(pow(10,5))]
for _ in range(Q):
    t,d,x=map(int, input().split())
    t-=1
    if d==0:
        www[t].append(x-1)
    else:
        hhh[t].append(x-1)
def calc(X,array):
    counts=[0]*X
    for sub in array:
        heapq.heapify(sub)
        tmp=[]
        while sub:
            x=heapq.heappop(sub)
            tmp.append(x)
            if x==0:
                counts[x]=INF
            else:
                counts[x]=counts[x-1]+1
        sub=tmp
        while sub:
            x=sub.pop()
            if x==X-1:
                counts[x]=min(counts[x],INF)
            else:
                counts[x]=min(counts[x],counts[x+1]+1)
    return counts
w_counts=calc(W,www)
h_counts=calc(H,hhh)
ret=min(w_counts)+min(h_counts)
if ret>=INF:
    print(-1)
else:
    print(ret)
