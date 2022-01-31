import collections
N=int(input())
jobs=collections.defaultdict(list)
ab_set=set()
for i in range(N):
    a,b=map(int, input().split())
    jobs[b].append((a,i+1))
    ab_set.add(a)
    ab_set.add(b)
ab_array=sorted(list(ab_set))
ab_compress={}
for i,a in enumerate(ab_array):
    ab_compress[a]=i
new_jobs=collections.defaultdict(list)
for b in jobs:
    for a,i in jobs[b]:
        new_jobs[ab_compress[b]].append((ab_compress[a],i))
jobs=new_jobs
dp=[(0,N*2,N*2)]*(len(ab_array)+1)
for t in range(len(ab_array),0,-1):
    c,next,_=dp[t]
    for a,i in jobs[t]:
        v=(c-1,i,t)
        dp[a]=min(dp[a],v)
    v=dp[t]
    a=t-1
    dp[a]=min(dp[a],v)
print(-dp[0][0])
rets=[]
now=0
while len(rets)<-dp[0][0]:
    rets.append(dp[now][1])
    now=dp[now][2]
print(*rets)
