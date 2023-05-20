import itertools
import collections
N=int(input())
blocks=[[0]*1001 for _ in range(1001)]
for _ in range(N):
    lx,ly,rx,ry=map(int, input().split())
    for x in range(lx,rx):
        blocks[x][ly]+=1
        blocks[x][ry]-=1
rets=[0]*(N+1)
for i in range(1001):
    acc=list(itertools.accumulate(blocks[i]))
    counts=collections.Counter(acc)
    for c in counts:
        rets[c]+=counts[c]
for i in range(1,N+1):
    print(rets[i])
