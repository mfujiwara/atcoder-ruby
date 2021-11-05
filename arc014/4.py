import bisect
import collections
ALL,N,M=map(int, input().split())
ls=[]
for _ in range(N):
    l=int(input())
    ls.append(l)
head=ls[0]-1
tail=ALL-ls[-1]
space=collections.defaultdict(int)
for i in range(N-1):
    diff=ls[i+1]-ls[i]
    space[diff-1]+=1
keys=sorted(list(space.keys()))
sums={}
total=(0,0)
for key in keys:
    n=space[key]
    total=(total[0]+key*n,total[1]+n)
    sums[key]=total
for _ in range(M):
    x,y=map(int, input().split())
    ret=N
    ret+=min(head,x)
    ret+=min(tail,y)
    index=bisect.bisect_right(keys,x+y)
    if index==0:
        ret+=(x+y)*(N-1)
    else:
        s,n=sums[keys[index-1]]
        ret+=s
        ret+=(x+y)*(N-1-n)
    print(ret)
