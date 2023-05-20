import collections
import itertools
N,M=map(int, input().split())
array=list(map(int, input().split()))
a2index=collections.defaultdict(list)
memo=[0]*(M+2)
rets=[0]*(M+1)
for i in range(N-1):
    a2index[array[i+1]].append(i+1)
    memo[array[i]+1]+=1
    if array[i]<array[i+1]:
        memo[array[i+1]]-=1
    else:
        memo[-1]-=1
        memo[1]+=1
        memo[array[i+1]]-=1
    rets[1]+=min((array[i+1]-array[i]+M)%M,array[i+1])
memo=list(itertools.accumulate(memo))
for i in range(2,M+1):
    v=rets[i-1]
    for index in a2index[i-1]:
        v+=(array[index]-array[index-1]+M)%M-1
    v-=memo[i-1]
    rets[i]=v
print(min(rets[1:]))
