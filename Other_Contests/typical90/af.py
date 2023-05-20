import itertools
INF=pow(10,10)
N=int(input())
A=[list(map(int, input().split())) for _ in range(N)]
M=int(input())
pair=set()
for _ in range(M):
    x,y=map(int, input().split())
    x-=1
    y-=1
    pair.add((x,y))
    pair.add((y,x))
ret=INF
for perm in itertools.permutations([i for i in range(N)],N):
    r=0
    valid=True
    for i in range(N):
        if i==0:
            r+=A[perm[i]][i]
        else:
            if (perm[i],perm[i-1]) in pair:
                valid=False
                break
            else:
                r+=A[perm[i]][i]
    if valid:
        ret=min(ret,r)
if ret==INF:
    print(-1)
else:
    print(ret)
