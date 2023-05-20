N=int(input())
array=list(map(int, input().split()))
iru=[1]*N*N
costs=[0]*N*N
for i in range(N):
    for j in range(N):
        costs[i*N+j]=min([i,j,N-1-i,N-1-j])
ret=0
for a in array:
    a-=1
    ij=a
    ret+=costs[ij]
    iru[ij]=0
    targets=[ij]
    while targets:
        tij=targets.pop()
        for dij in [N,-N,1,-1]:
            uij=tij+dij
            if 0<=uij<N*N:
                x=costs[tij]+iru[tij]
                if costs[uij]>x:
                    costs[uij]=x
                    targets.append(uij)
print(ret)
