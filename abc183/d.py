import itertools
N,W=map(int, input().split())
memo=[0]*(2*pow(10,5)+1)
for _ in range(N):
    s,t,p=map(int, input().split())
    memo[s]+=p
    memo[t]-=p
if max(itertools.accumulate(memo))<=W:
    print("Yes")
else:
    print("No")
