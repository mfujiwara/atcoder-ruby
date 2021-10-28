N,M=map(int, input().split())
edges=[[0]*N for i in range(N)]
for _ in range(M):
    a,b=map(int, input().split())
    a,b=a-1,b-1
    edges[a][b]=1
    edges[b][a]=1
memo=[-1]*pow(2,N)
for bits in range(1,pow(2,N)):
    sss=list()
    k=bits
    i=0
    while k>0:
        if k&1!=0:
            sss.append(i)
        k//=2
        i+=1
    if len(sss)==1:
        memo[bits]=1
        continue
    valid=True
    for i in range(len(sss)-1):
        for j in range(i+1,len(sss)):
            if edges[sss[i]][sss[j]]==0:
                valid=False
                break
        if not valid:
            break
    if valid:
        memo[bits]=1
        continue
    b1=bits
    r=len(sss)
    while b1>0:
        b1=(b1-1)&bits
        b2=bits-b1
        if b1<b2:
            break
        r=min(r,memo[b1]+memo[b2])
    memo[bits]=r
print(memo[pow(2,N)-1])
