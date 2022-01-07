import collections
N,M=map(int, input().split())
array=list(map(int, input().split()))
edges=collections.defaultdict(list)
for _ in range(M):
    x,y=map(int, input().split())
    edges[x-1].append(y-1)
buy=[10**10]*N
ret=-10**9
for i in range(N):
    ret=max(ret,array[i]-buy[i])
    for j in edges[i]:
        buy[j]=min(buy[j],buy[i],array[i])
print(ret)
