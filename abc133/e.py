import sys
sys.setrecursionlimit(500000)
MOD=10**9+7
N,K=map(int, input().split())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
done=[False]*N

targets=[(0,0,0)] # index, d1, d2
done[0]=True
ret=1
while targets:
    t,n1,n2=targets.pop()
    ret*=(K-n1-n2)
    ret%=MOD
    c=0
    for a in edges[t]:
        if done[a]: continue
        targets.append((a,1,n1+c))
        done[a]=True
        c+=1
print(ret)
