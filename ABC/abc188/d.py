import collections
N,C=map(int, input().split())
memo=collections.defaultdict(int)
for _ in range(N):
    a,b,c=map(int, input().split())
    memo[a]+=c
    memo[b+1]-=c
ret=0
now=0
cost=0
for key in sorted(list(memo.keys())):
    ret+=min(cost,C)*(key-now)
    cost+=memo[key]
    now=key
print(ret)
