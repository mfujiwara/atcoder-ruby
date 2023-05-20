import collections
N=int(input())
dates=collections.defaultdict(int)
for _ in range(N):
    a,b=map(int, input().split())
    dates[a]+=1
    dates[a+b]-=1

rets=[0]*N
now=0
pre_d=0
for d in sorted(list(dates.keys())):
    if now!=0:
        rets[now-1]+=d-pre_d
    now+=dates[d]
    pre_d=d
print(*rets)
