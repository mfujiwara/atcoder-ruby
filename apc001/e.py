import collections
N=int(input())
if N==2:
  print(1)
  exit()
edges=collections.defaultdict(list)
for _ in range(N-1):
  a,b=map(int,input().split())
  edges[a].append(b)
  edges[b].append(a)
r=max(range(N),key=lambda i:len(edges[i]))
ret=0
memo=[None]*N
targets=[(r,-1,0)]
while targets:
    u,p,s=targets.pop()
    if s==0:
        targets.append((u,p,1))
        for t in edges[u]:
            if t==p:
                continue
            targets.append((t,u,0))
    else:
        c=0
        for t in edges[u]:
            if t==p:
                continue
            c+=memo[t]
        # 枝を識別する必要があるため、枝の数-1が必要
        ret+=max(c-1,0)
        if len(edges[u])==1 or len(edges[u])==2 and c==1:
            # 葉を伝播させる
            memo[u]=1
        else:
            memo[u]=0
print(ret)
