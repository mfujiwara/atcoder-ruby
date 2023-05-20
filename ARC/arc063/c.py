
import collections
import heapq
N=int(input())
edges_list=[]
edges=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    edges[a].append(b)
    edges[b].append(a)
    edges_list.append((a,b))
K=int(input())
vals=[-1]*N
for _ in range(K):
    v,p=map(int, input().split())
    vals[v-1]=p
targets=[] # (val,v)
for a,b in edges_list:
    va=vals[a]
    vb=vals[b]
    if va==-1 and vb==-1: continue
    if va==-1:
        targets.append((vb,b))
        continue
    if vb==-1:
        targets.append((va,a))
        continue
    if abs(va-vb)!=1:
        print("No")
        exit()
heapq.heapify(targets)
#print(targets)
while targets:
    _,t=heapq.heappop(targets)
    for u in edges[t]:
        if vals[u]==-1:
            vals[u]=vals[t]+1
            heapq.heappush(targets,(vals[u],u))
        else:
            if abs(vals[u]-vals[t])!=1:
                print("No")
                exit()
print("Yes")
for v in vals:
    print(v)
