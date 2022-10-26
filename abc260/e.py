import collections
import itertools
N,M=map(int, input().split())
ab=collections.defaultdict(int)
max_a=0
min_b=M
for _ in range(N):
    a,b=map(int, input().split())
    ab[a]=max(ab[a],b)
    max_a=max(max_a,a)
    min_b=min(min_b,b)
end=max_a
count=0
rets=[0]*(M+1)
for start in range(1,min_b+1):
    #print((start,end))
    # start..end から start..M までで全部含んでいる
    rets[end-start]+=1
    rets[M-start+1]-=1
    #次のstartで必要になるb
    end=max(end,ab[start])
rets=list(itertools.accumulate(rets))
rets.pop()
print(*rets)
