MOD=998244353
N=int(input())
array=list(map(lambda e: int(e)-1, input().split()))
ret=1
g=0
group=[-1]*N
for i in range(N):
    g+=1
    if group[i]!=-1: continue
    a=i
    while group[a]==-1:
        group[a]=g
        a=array[a]
    if group[a]==g:
        ret*=2
        ret%=MOD
print(ret-1)
