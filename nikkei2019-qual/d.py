from collections import defaultdict
N,M=map(int, input().split())
a_count=[0]*N
b_count=[0]*N
edges=defaultdict(list)
for i in range(N-1+M):
    a,b=map(int, input().split())
    a_count[a-1]+=1
    b_count[b-1]+=1
    edges[a-1].append(b-1)
root=-1
for i in range(N):
    if b_count[i]==0:
        root=i
        break
parents=[-1]*N
parents[root]=-1
targets=[root]
while targets:
    t=targets.pop()
    nexts=edges[t]
    for n in nexts:
        if b_count[n]==1:
            targets.append(n)
            parents[n]=t
        b_count[n]-=1
for p in parents:
    print(p+1)
