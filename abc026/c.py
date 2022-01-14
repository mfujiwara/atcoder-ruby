N=int(input())
min_max=[[0,0] for _ in range(N)]
parent=[-1]*N
for i in range(1,N):
    b=int(input())
    parent[i]=b-1
for i in range(N-1,0,-1):
    b=parent[i]
    r=sum(min_max[i])+1
    if min_max[b][0]==0:
        min_max[b][0]=r
    else:
        min_max[b][0]=min(min_max[b][0],r)
    min_max[b][1]=max(min_max[b][1],r)
print(sum(min_max[0])+1)
