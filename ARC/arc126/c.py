import itertools
N,K=map(int, input().split())
array=list(map(int, input().split()))
array.sort()
total=sum(array)
counts=[0]*(array[-1]+1)
for a in array:
    counts[a]+=1
sums=list(itertools.accumulate(counts))
ret=1
for i in range(2, array[-1]):
    target=0
    t=i
    while t<array[-1]:
        target+=(sums[t]-sums[t-i])*t
        t+=i
    target+=(N-sums[t-i])*t
    r=target-total
    if r<=K:
        ret=i
if array[-1]*N-total<=K:
    ret=(K+total)//N
print(ret)
