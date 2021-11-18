import collections
N=int(input())
edges=[[False]*N for _ in range(N)]
for i in range(N):
    for j,ch in enumerate(input()):
        if i==j or ch=="1":
            edges[i][j]=True
for i in range(N):
    targets=[ j for j,b in enumerate(edges[i]) if b ]
    while targets:
        t=targets.pop()
        for u in [ j for j,b in enumerate(edges[t]) if b ]:
            if edges[i][u]: continue
            edges[i][u]=True
            targets.append(u)
ret=0
for i in range(N):
    c=0
    for j in range(N):
        if edges[j][i]:
            c+=1
    ret+=1/c
print(ret)
