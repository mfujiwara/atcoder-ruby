import bisect
import itertools
INF=pow(10,18)
N,M=map(int, input().split())
weights=list(map(int, input().split()))
mini_v=INF
vl=[]
for _ in range(M):
    l,v=map(int, input().split())
    vl.append((v,l))
    mini_v=min(mini_v,v)
if max(weights)>mini_v:
    print(-1)
    exit()
vl.sort(key=lambda e: (e[0],-e[1]))
for i in range(1,M):
    if vl[i][1]<vl[i-1][1]:
        vl[i]=(vl[i][0],vl[i-1][1])
ret=INF
for perm in itertools.permutations(weights):
    dp=[0]*N
    for i in range(1,N):
        v=0
        for j in range(i,-1,-1):
            v+=perm[j]
            t=bisect.bisect_right(vl,(v-1,INF))
            if t>0:
                dp[i]=max(dp[i], dp[j]+vl[t-1][1])
    ret=min(ret,dp[-1])
print(ret)
