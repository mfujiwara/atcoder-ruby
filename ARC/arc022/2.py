from collections import defaultdict
N=int(input())
array=list(map(int, input().split()))
memo=defaultdict(lambda:-1)
start=0
ret=0
for i,a in enumerate(array):
    pre=memo[a]
    if pre!=-1 and pre>=start:
        r=i-start
        ret=max(ret,r)
        start=pre+1
    memo[a]=i
ret=max(ret,N-start)
print(ret)
